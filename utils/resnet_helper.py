# utils/resnet_helper.py
import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# ✅ Preprocessing transform for ResNet50
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# ✅ Load pretrained ResNet50 (cached locally)
def load_resnet50():
    model_path = "models/resnet50_imagenet.pth"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    os.makedirs("models", exist_ok=True)

    if not os.path.exists(model_path):
        import urllib.request
        url = "https://download.pytorch.org/models/resnet50-0676ba61.pth"
        print("⬇️ Downloading ResNet50 weights...")
        urllib.request.urlretrieve(url, model_path)

    try:
        model = models.resnet50(weights=None)
        if os.path.exists(model_path):
            # Load locally saved weights
            model.load_state_dict(torch.load(model_path, map_location=device))
            print("✅ Loaded ResNet50 from local weights.")
        else:
            # Download and save pretrained weights
            pretrained = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
            torch.save(pretrained.state_dict(), model_path)
            model.load_state_dict(pretrained.state_dict())
            print("📥 Downloaded and saved pretrained ResNet50 weights.")
    except Exception as e:
        print(f"⚠️ Error loading weights: {e}")
        model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)

    model.eval().to(device)
    return model


# ✅ Convert image to tensor
def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    img_t = preprocess(image).unsqueeze(0)
    return img_t


# ✅ Run classification on single image
def classify_image(model, img_t, labels=None):
    device = next(model.parameters()).device
    with torch.no_grad():
        outputs = model(img_t.to(device))
        _, predicted = outputs.max(1)

    pred_idx = predicted.item()
    if labels and 0 <= pred_idx < len(labels):
        return labels[pred_idx]
    else:
        return f"Class {pred_idx}"
