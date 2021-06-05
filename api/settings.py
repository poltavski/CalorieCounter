"""Settings for api service."""
import pickle

FOOD_101_CLASSES_PATH = "../networks/food-101/food101_classes.data"
FOOD_101_MODEL_PATH = "../networks/food-101/model_19.pt"
FOOD_101_CLASSES = None

IMAGE_FOLDER = "images"
NOT_FOUND_IMAGE = "default.jpg"
INFERENCE_THRESHOLD = 0.5
MODEL_DIR = "../networks/u2net/u2netp.pth"


with open(FOOD_101_CLASSES_PATH, "rb") as filehandle:
    # read the data as binary data stream
    FOOD_101_CLASSES = pickle.load(filehandle)
