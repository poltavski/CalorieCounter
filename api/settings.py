"""Settings for api service."""
import pickle
import os
from dotenv import load_dotenv

load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')

FOOD_101_CLASSES = None
FOOD_101_CLASSES_PATH = "api/networks/food-101/food101_classes.data"
FOOD_101_MODEL_PATH = "api/networks/food-101/model_19.pt"

FOOD_500_CLASSES = None
FOOD_500_CLASSES_PATH = "api/networks/food_500/food_500_classes.txt"
FOOD_500_MODEL_PATH = "api/networks/food_500/food_500_model.pth"

IMAGE_FOLDER = "api/images"
INFERENCE_THRESHOLD = 0.5
MODEL_DIR = "api/networks/u2net/u2netp.pth"
NOT_FOUND_IMAGE = "default.jpg"
RESULT_NAME = "result"
STATIC_FOLDER = "api/_static"

DETALIZATION = 1
# Verbosity means how server treat masked objects:
# 0 - Return standard location response
# 1 - Save requested image and response image


with open(FOOD_101_CLASSES_PATH, "rb") as filehandle:
    # read the data as binary data stream
    FOOD_101_CLASSES = pickle.load(filehandle)

with open(FOOD_500_CLASSES_PATH, "r") as f:
    lines = f.readlines()
    FOOD_500_CLASSES = [line.split('\t')[0] for line in lines]
