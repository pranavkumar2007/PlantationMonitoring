import os
import cv2
cv2.setNumThreads(0)
# ======= Imports =======
import streamlit as st
import shutil
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_image_coordinates import streamlit_image_coordinates
from utils.sam_helper import load_sam, run_sam, overlay_masks_on_image, run_sam_click
from utils.resnet_helper import load_resnet50, preprocess_image, classify_image

def show_dashboard():
    
    st.title("🌱 Plantation Monitoring (SAM Segmenter + RESNET50 Classification)")

    st.markdown("""
    <div class="info-card">
        <strong>📸 Upload Your Plantation Image</strong><br>
        Use Meta's <strong>Segment Anything Model (SAM)</strong> to segment plantation regions automatically or manually.
        <br><br>
        <em>⚡ Note: SAM runs faster on GPU. Expect slower performance on CPU.</em>
    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # Load SAM Model
    # -----------------------------------------------------
    if "mask_generator" not in st.session_state:
        with st.spinner("🔄 Loading SAM model (please wait 20–60s)..."):
            st.session_state.mask_generator = load_sam("models/sam_vit_b.pth")
        st.success("✅ SAM model loaded successfully!")

    if "resnet_model" not in st.session_state:
        with st.spinner("🧠 Loading ResNet50 model..."):
            st.session_state.resnet_model = load_resnet50()
        st.success("✅ ResNet50 model loaded successfully!")
        
    # Load ImageNet labels
    if os.path.exists("imagenet_classes.txt"):
        with open("imagenet_classes.txt") as f:
            imagenet_labels = [line.strip() for line in f.readlines()]
    else:
        imagenet_labels = [f"Class {i}" for i in range(1000)]

    # -----------------------------------------------------
    # File Upload
    # -----------------------------------------------------
    uploaded = st.file_uploader("📁 Choose an image file", type=["jpg", "jpeg", "png"])

    def resize_for_sam(img_np, max_dim=1024):
        h, w = img_np.shape[:2]
        if max(h, w) > max_dim:
            scale = max_dim / max(h, w)
            new_w, new_h = int(w * scale), int(h * scale)
            return cv2.resize(img_np, (new_w, new_h), interpolation=cv2.INTER_AREA)
        return img_np

    # -----------------------------------------------------
    # Mode Selection
    # -----------------------------------------------------
    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        img_np = np.array(image)
        st.markdown("---")
        st.image(image, caption="Uploaded plantation image", width='stretch')

        mode = st.radio(
            "Select Segmentation Mode:",
            ["Automatic (Detect all regions)", "Manual (Click-based selection)"],
            horizontal=True
        )

        # -------------------------------------------------
        # Automatic Segmentation
        # -------------------------------------------------
        if mode == "Automatic (Detect all regions)":
            if st.button("🚀 Run SAM Segmentation"):
                with st.spinner("🔬 Running segmentation…"):
                    img_for_sam = resize_for_sam(img_np)
                    masks = run_sam(st.session_state.mask_generator, img_for_sam)

                if len(masks) == 0:
                    st.warning("⚠️ No masks detected — try another image.")
                else:
                    st.success(f"✅ Segmentation complete — {len(masks)} masks detected!")
                    overlay = overlay_masks_on_image(img_for_sam, masks, alpha=0.55)
                    st.image(overlay, caption="AI-generated segmentation overlay", width='stretch')

                    # Prepare output directory
                    output_dir = "output_segments"
                    if os.path.exists(output_dir):
                        shutil.rmtree(output_dir)
                    os.makedirs(output_dir, exist_ok=True)

                    results = []
                    st.markdown("### 💾 Saving & Classifying Segments…")
                    progress = st.progress(0)

                    for i, m in enumerate(masks):
                        seg = m["segmentation"]
                        ys, xs = np.where(seg)
                        if ys.size == 0 or xs.size == 0:
                            continue
                        y0, y1 = ys.min(), ys.max()
                        x0, x1 = xs.min(), xs.max()
                        crop = img_for_sam[y0:y1 + 1, x0:x1 + 1]

                        save_path = os.path.join(output_dir, f"segment_{i + 1}.png")
                        cv2.imwrite(save_path, cv2.cvtColor(crop, cv2.COLOR_RGB2BGR))

                        # Classify with ResNet50
                        img_t = preprocess_image(save_path)
                        label = classify_image(st.session_state.resnet_model, img_t, imagenet_labels)
                        results.append((f"Segment {i + 1}", label, save_path))

                        progress.progress((i + 1) / len(masks))

                    # ✅ Display results in grid
                    st.markdown("### 🌿 Classified Segments")
                    cols = st.columns(3)
                    for idx, (name, label, path) in enumerate(results):
                        with cols[idx % 3]:
                            st.image(path, caption=f"{name}: {label}", width='stretch')

                    # 📊 Visualization
                    df = pd.DataFrame(results, columns=["Segment", "Label", "Path"])
                    fig, ax = plt.subplots(figsize=(7, 4))
                    df["Label"].value_counts().head(10).plot(kind="bar", color="#00ffff", ax=ax)
                    plt.title("Crop Type Distribution")
                    plt.xlabel("Crop Type")
                    plt.ylabel("Count")
                    st.pyplot(fig)

                    # 📥 CSV Download
                    csv = df[["Segment", "Label"]].to_csv(index=False).encode("utf-8")
                    st.download_button("📥 Download Classification Results", csv, "classification_results.csv", "text/csv")
                    st.success(f"✅ Classified {len(results)} segments successfully!")

        # -------------------------------------------------
        # Manual (Click-based) Segmentation
        # -------------------------------------------------
        else:
            st.markdown("### 🎯 Click on the image to select a region")
            click = streamlit_image_coordinates(image, key="click_image")

            if click is not None:
                x, y = int(click["x"]), int(click["y"])
                st.info(f"🖱️ Clicked at coordinates: (X={x}, Y={y})")

                if st.button("✂️ Segment Selected Object"):
                    from utils.sam_helper import run_sam_click
                    with st.spinner("Running SAM click-based segmentation..."):
                        masks = run_sam_click("models/sam_vit_b.pth", np.array(image), x, y)

                    if len(masks) > 0:
                        mask = masks[0]
                        mask_vis = np.array(image).copy()
                        color = np.array([0, 255, 0], dtype=np.uint8)
                        mask_vis[mask] = (mask_vis[mask] * 0.4 + color * 0.6).astype(np.uint8)
                        st.image(mask_vis, caption="Selected object segmented", width='stretch')
                        st.success("✅ Object segmented successfully!")
                    else:
                        st.warning("⚠️ No object detected at this point.")
            else:
                st.info("👆 Click anywhere on the image to start segmentation.")
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <p style='color: #666; margin-bottom: 0.5rem;'>Connect with us on social media</p>
        <p style='font-size: 1.5rem;'>
            🌐 💼 📱 
        </p>
        <p style='color: #999; font-size: 0.9rem; margin-top: 1rem;'>
            © 2025 Plantation Monitoring System. All rights reserved.
        </p>
    </div>
    """, unsafe_allow_html=True)
