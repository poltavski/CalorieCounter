import logging
import os
import requests
import sys
import uvicorn
from typing import Dict, Union
from functools import wraps
from api.models import FoodClassification, SalientObjectDetection
from fastapi import FastAPI, HTTPException, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from io import BytesIO
from PIL import Image
from api.settings import (
    STATIC_FOLDER,
    FOOD_101_CLASSES,
    FOOD_101_MODEL_PATH,
)
from api.utils import label_processing, mask_processing, get_food_table

sys.setrecursionlimit(1500)
logging.basicConfig(
    filename="server.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s: %(funcName)s - %(levelname)s - %(message)s",
)

os.makedirs(STATIC_FOLDER, exist_ok=True)
app = FastAPI(title="CalorieCounter", version="1.0.1")
app.mount("/_static", StaticFiles(directory=STATIC_FOLDER), name="_static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

food_classifier_101 = FoodClassification(FOOD_101_MODEL_PATH, FOOD_101_CLASSES)
sod = SalientObjectDetection()


def error_handling(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Following error occurred on server: {e}. Please contact support",
            )
    return wrapper


@app.get("/")
async def ping():
    """
    ## Ping API call.

    ### Returns:
        200
    """
    return


@app.post("/image/label/byte")
@error_handling
async def inference_demo(
    byte_image: bytes = File(...),
    percentage: bool = False,
) -> Union[Dict[str, float], Dict[str, str]]:
    """
    ## Public endpoint for food image labeling by POST request.

    ### Args:
        byte_image: image bytes
        percentage: show probabilities in percentage

    ### Returns:
        Dictionary with image labels and probabilities
    """
    image = Image.open(BytesIO(byte_image)).convert("RGB")
    return label_processing(image, food_classifier_101, percentage)


@app.get("/image/label/url")
@error_handling
async def inference_demo(
    url: str = "https://i.pinimg.com/originals/36/a3/2e/36a32e2efcfce9a2d5daa5ebf1a7b31e.jpg",
    percentage: bool = False,
) -> Union[Dict[str, float], Dict[str, str]]:
    """
    ## Public endpoint for food image labeling by GET request.

    ### Args:
        url: image url
        percentage: show probabilities in percentage

    ### Returns:
        Dictionary with image labels and probabilities
    """
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    return label_processing(image, food_classifier_101, percentage)


@app.post("/image/mask/byte")
@error_handling
async def inference_demo(
    byte_image: bytes = File(...),
    food_restriction: bool = True,
) -> FileResponse:
    """
    ## Public endpoint for food image segmentation by POST request.

    ### Args:
        byte_image: image bytes

    ### Returns:
        Image (.jpg)
    """
    image = Image.open(BytesIO(byte_image)).convert("RGB")
    return FileResponse(
        mask_processing(image, sod, food_classifier_101, food_restriction)
    )


@app.get("/image/mask/url")
@error_handling
async def inference_demo(
    url: str = "https://i.pinimg.com/originals/36/a3/2e/36a32e2efcfce9a2d5daa5ebf1a7b31e.jpg",
    food_restriction: bool = True,
) -> FileResponse:
    """
    ## Public endpoint for food image segmentation by GET request.

    ### Args:
        url: image url

    ### Returns:
        Image (.jpg)
    """
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    return FileResponse(
        mask_processing(image, sod, food_classifier_101, food_restriction)
    )


@app.get("/db/food")
@error_handling
async def inference_demo() -> dict:
    """
    ## Public endpoint for food image segmentation by GET request.

    ### Args:
        url: image url

    ### Returns:
        Image (.jpg)
    """
    return get_food_table()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")
