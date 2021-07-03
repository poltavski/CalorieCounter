import numpy as np
import torch
from networks.u2net.data_loader import RescaleT
from networks.u2net.data_loader import ToTensorLab

# U2net full size version 173.6 MB vs small version u2netp 4.7 MB
from networks.u2net.u2net import U2NET, U2NETP

from PIL import Image
from settings import FOOD_101_CLASSES, FOOD_101_MODEL_PATH, MODEL_DIR
from torch.autograd import Variable
from torchvision import transforms
from typing import Any, Dict, List, Union


class FoodClassification:
    """Food classification model class."""

    def __init__(self):
        self.classifier = self.load_classifier(FOOD_101_MODEL_PATH)
        self.classes = FOOD_101_CLASSES
        print("Food classification loaded.")

    def predict(self, image: np.array, n_top: int = 5) -> Dict[str, Any]:
        """Recognize food labels/probabilities from image."""
        classifier = self.classifier
        tensor = self.transform_image(image=image)
        outputs = classifier.forward(tensor)
        sm = torch.nn.Softmax(dim=1)
        probabilities = torch.flatten(sm(outputs))
        probs, labels = torch.topk(probabilities, n_top)
        labels = labels.cpu().detach().numpy()
        probs = probs.cpu().detach().numpy()
        results = {
            FOOD_101_CLASSES[labels[i]]: round(float(probs[i]), 4) for i in range(n_top)
        }
        return results

    @staticmethod
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

    @staticmethod
    def load_classifier(model_path):
        model = torch.load(model_path)
        model.eval()
        return model


class SalientObjectDetection:
    """Salient Object Detection u^2net model inference."""

    def __init__(self, u2netp: bool = True):
        self.net = U2NETP(3, 1) if u2netp else U2NET(3, 1)
        self.net.load_state_dict(torch.load(MODEL_DIR))
        if torch.cuda.is_available():
            self.net.cuda()
        self.net.eval()

    def predict(self, image):
        # Ensure i,qge size is under 1024
        if image.size[0] > 1024 or image.size[1] > 1024:
            image.thumbnail((1024, 1024))

        torch.cuda.empty_cache()

        sample = self.preprocess(np.array(image))
        inputs_test = sample["image"].unsqueeze(0)
        inputs_test = inputs_test.type(torch.FloatTensor)

        if torch.cuda.is_available():
            inputs_test = Variable(inputs_test.cuda())
        else:
            inputs_test = Variable(inputs_test)

        d1, d2, d3, d4, d5, d6, d7 = self.net(inputs_test)

        # Normalization.
        pred = d1[:, 0, :, :]
        predict = self.norm_prediction(pred)

        # Convert to PIL Image
        predict = predict.squeeze()
        predict_np = predict.cpu().data.numpy()
        im = Image.fromarray(predict_np * 255).convert("RGB")

        # Cleanup.
        del d1, d2, d3, d4, d5, d6, d7

        return im

    @staticmethod
    def norm_prediction(d):
        ma = torch.max(d)
        mi = torch.min(d)
        dn = (d - mi) / (ma - mi)
        return dn

    @staticmethod
    def preprocess(image):
        label_3 = np.zeros(image.shape)
        label = np.zeros(label_3.shape[0:2])

        if 3 == len(label_3.shape):
            label = label_3[:, :, 0]
        elif 2 == len(label_3.shape):
            label = label_3

        if 3 == len(image.shape) and 2 == len(label.shape):
            label = label[:, :, np.newaxis]
        elif 2 == len(image.shape) and 2 == len(label.shape):
            image = image[:, :, np.newaxis]
            label = label[:, :, np.newaxis]

        transform = transforms.Compose([RescaleT(320), ToTensorLab(flag=0)])
        sample = transform({"imidx": np.array([0]), "image": image, "label": label})

        return sample
