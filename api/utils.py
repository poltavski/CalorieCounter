import torch
import numpy as np
from typing import Any, Dict, List, Union
from settings import FOOD_101_CLASSES, FOOD_101_MODEL_PATH
import torchvision.transforms as transforms
from PIL import Image, ImageOps

class FoodClassification:
    def __init__(self):
        self.classifier = load_classifier(FOOD_101_MODEL_PATH)
        self.classes = FOOD_101_CLASSES
        print("Food classification loaded.")

    def predict(
        self, image: np.array
    ) -> Dict[str, Any]:
        """Recognize food label from image."""
        results = {}
        classifier = self.classifier
        tensor = transform_image(image=image)
        outputs = classifier.forward(tensor)
        _, pred = outputs.max(1)
        predicted_label = FOOD_101_CLASSES[pred]
        results["class"] = predicted_label
        return results


def transform_image(image: np.array):
    """Sends tensor to cuda."""
    my_transforms = transforms.Compose(
        [transforms.Resize(320),
        transforms.CenterCrop(299),
        transforms.ToTensor(),
        transforms.Normalize(
            [0.485, 0.456, 0.406],
            [0.229, 0.224, 0.225])]
    )
    tensor = my_transforms(image).unsqueeze(0)
    tensor = tensor.cuda()
    return tensor


def load_classifier(model_path):
    model = torch.load(model_path)
    model.eval()
    return model


def visualize_mask(orig_image, pred_image):
    mask = Image.new("L", orig_image.size, 128)
    pred_image = ImageOps.colorize(pred_image.convert('L'), black="black", white="green")
    print(orig_image.size, pred_image.size)
    # if not match
    pred_image = pred_image.resize(orig_image.size)
    result = Image.composite(orig_image, pred_image, mask)
    return result