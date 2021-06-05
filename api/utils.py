import numpy as np
import torch
import torchvision.transforms as transforms

from models.u2nethttp import u2net
from PIL import Image, ImageOps
from settings import FOOD_101_CLASSES, FOOD_101_MODEL_PATH
from typing import Any, Dict, List, Union


class FoodClassification:
    def __init__(self):
        self.classifier = load_classifier(FOOD_101_MODEL_PATH)
        self.classes = FOOD_101_CLASSES
        print("Food classification loaded.")

    def predict(self, image: np.array) -> Dict[str, Any]:
        """Recognize food label from image."""
        results = {}
        classifier = self.classifier
        tensor = transform_image(image=image)
        outputs = classifier.forward(tensor)
        _, pred = outputs.max(1)
        predicted_label = FOOD_101_CLASSES[pred]
        results["class"] = predicted_label
        return results


def analyze(image: Image):
    """Perform inference on image.

    Args:
        image: Image,
            provided image

    Returns:
        dict of recognized properties of vehicle items.
    """
    # Ensure i,qge size is under 1024
    if image.size[0] > 1024 or image.size[1] > 1024:
        image.thumbnail((1024, 1024))

    # Process Image
    results = u2net.run(np.array(image))
    return results


def transform_image(image: np.array):
    """Sends tensor to cuda."""
    my_transforms = transforms.Compose(
        [
            transforms.Resize(320),
            transforms.CenterCrop(299),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )
    tensor = my_transforms(image).unsqueeze(0)
    tensor = tensor.cuda()
    return tensor


def load_classifier(model_path):
    model = torch.load(model_path)
    model.eval()
    return model


def visualize_mask(
    orig_image, pred_image, resize: bool = False, size: tuple = (320, 320)
):
    """Visualize mask on image. Resize by option

    Args:
        orig_image:
        pred_image:
        resize:
        size:

    Returns:
        Image with mask
    """
    mask = Image.new("L", orig_image.size, 128)
    pred_image = ImageOps.colorize(
        pred_image.convert("L"), black="black", white="green"
    )
    pred_image = pred_image.resize(orig_image.size)
    result = Image.composite(orig_image, pred_image, mask)
    if resize:
        result = result.resize(size, Image.ANTIALIAS)
    return result
