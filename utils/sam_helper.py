import torch
import numpy as np
import urllib.request
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
import streamlit as st
import os

def get_device():
    return "cuda" if torch.cuda.is_available() else "cpu"


# -----------------------------------------------------
# 1️⃣ LOAD SAM MODEL (Automatic Mask Generator)
# -----------------------------------------------------
@st.cache_resource
def load_sam(
    checkpoint_path="Fine Tuned SAM/fine_tuned_sam_vit_b_final.pth", 
    model_type="vit_b"
):
    """
    Loads the fine-tuned SAM model and returns a SamAutomaticMaskGenerator instance.
    Automatically downloads the base SAM if fine-tuned model not found.
    """

    # Ensure models folder exists
    os.makedirs("Fine Tuned SAM", exist_ok=True)

    # ✅ Check if fine-tuned model exists
    if not os.path.exists(checkpoint_path):
        print("[sam_helper] Fine-tuned SAM model not found — downloading base pretrained weights as fallback...")
        url = "https://huggingface.co/facebook/sam-vit-base/resolve/main/sam_vit_b_01ec64.pth"
        base_path = "Fine Tuned SAM/sam_vit_b_base.pth"
        try:
            urllib.request.urlretrieve(url, base_path)
            checkpoint_path = base_path
            print("[sam_helper] Base SAM model downloaded.")
        except Exception as e:
            raise RuntimeError(f"Failed to download fallback SAM model: {e}")

    # ✅ Load model to device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[sam_helper] Loading Fine-Tuned SAM ({model_type}) on {device} ...")

    sam = sam_model_registry[model_type](checkpoint=checkpoint_path)
    sam.to(device=device)
    mask_generator = SamAutomaticMaskGenerator(sam)

    print("[sam_helper] Fine-Tuned SAM loaded successfully.")
    return mask_generator



# -----------------------------------------------------
# 2️⃣ RUN AUTOMATIC SEGMENTATION
# -----------------------------------------------------
def run_sam(mask_generator, image_np):
    """
    Runs automatic mask generation on an image.
    image_np: uint8 RGB numpy array (H, W, 3)
    returns: list of mask dicts
    """
    masks = mask_generator.generate(image_np)
    return masks


# -----------------------------------------------------
# 3️⃣ OVERLAY MASKS (FOR DISPLAY)
# -----------------------------------------------------
def overlay_masks_on_image(image_np, masks, alpha=0.6):
    """
    Overlays all generated masks on the image with random colors.
    """
    overlay = image_np.copy()
    for m in masks:
        seg = m["segmentation"]
        color = np.random.randint(0, 255, size=(3,), dtype=np.uint8)
        overlay[seg] = (overlay[seg].astype(np.float32) * (1 - alpha) +
                        color.astype(np.float32) * alpha).astype(np.uint8)
    return overlay


# -----------------------------------------------------
# 4️⃣ MANUAL (CLICK-BASED) SEGMENTATION
# -----------------------------------------------------
def run_sam_click(checkpoint_path, image_np, click_x, click_y, model_type="vit_b"):
    """
    Runs SAM in manual mode for a single click point.
    click_x, click_y: coordinates of user click
    returns: list of masks for that click
    """
    device = get_device()
    print(f"[sam_helper] Running click-based SAM on {device} ...")

    sam = sam_model_registry[model_type](checkpoint=checkpoint_path)
    sam.to(device=device)
    predictor = SamPredictor(sam)
    predictor.set_image(image_np)

    # Define click point (x, y)
    input_point = np.array([[click_x, click_y]])
    input_label = np.array([1])  # 1 means foreground

    masks, scores, logits = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=True
    )

    print(f"[sam_helper] {len(masks)} masks generated from click.")
    return masks
