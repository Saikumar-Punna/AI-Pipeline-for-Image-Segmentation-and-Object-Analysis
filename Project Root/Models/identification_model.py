import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

class IdentificationModel:
    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    def identify(self, image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model.get_text_features(**inputs)
        return outputs

def describe_objects(image_paths):
    model = IdentificationModel()
    descriptions = {}
    for img_path in image_paths:
        desc = model.identify(img_path)
        descriptions[img_path] = desc
    return descriptions

if __name__ == "__main__":
    descriptions = describe_objects(["data/segmented_objects/object1.jpg", "data/segmented_objects/object2.jpg"])
    for path, desc in descriptions.items():
        print(f"Description for {path}: {desc}")

