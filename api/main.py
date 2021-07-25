import logging
import requests
import sys
import uvicorn

from datetime import datetime
from api.models import FoodClassification, SalientObjectDetection
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from io import BytesIO
from PIL import Image
from api.settings import IMAGE_FOLDER, INFERENCE_THRESHOLD, NOT_FOUND_IMAGE
from api.utils import visualize_mask


sys.setrecursionlimit(1500)
logging.basicConfig(
    filename="server.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s: %(funcName)s - %(levelname)s - %(message)s",
)

app = FastAPI(title="CalorieCounter", version="1.0.0")
app.mount("/_static", StaticFiles(directory="api/_static"), name="_static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

food_classifier = FoodClassification()
sod = SalientObjectDetection()


@app.get("/")
async def ping():
    """
    ## Ping api call.

    ### Returns:
        200
    """
    return


@app.get("/image/label")
async def inference_demo(
    url: str = "https://i.pinimg.com/originals/36/a3/2e/36a32e2efcfce9a2d5daa5ebf1a7b31e.jpg",
    percentage: bool = True,
):
    """
    ## Public endpoint for food image labeling by GET request.

    ### Args:
        url: image url
        percentage: show probabilities in percentage

    ### Returns:
        Dictionary with image labels and probabilities
    """
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content)).convert("RGB")
        result = food_classifier.predict(image)
        if percentage:
            for key, value in result.items():
                result[key] = f"{round(value*100)}%"
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Following error occurred on server: {e}. Please contact support",
        )


@app.get("/image/mask")
async def inference_demo(
    url: str = "https://i.pinimg.com/originals/36/a3/2e/36a32e2efcfce9a2d5daa5ebf1a7b31e.jpg",
    food_restriction: bool = True,
):
    """
    ## Public endpoint for food image segmentation by GET request.

    ### Args:
        url: image url

    ### Returns:
        Image (.jpg)
    """
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content)).convert("RGB")
        food = not food_restriction
        result_name = "result"
        if food_restriction:
            result = food_classifier.predict(image)
            food = (
                True
                if result and next(iter(result.values())) > INFERENCE_THRESHOLD
                else False
            )
            if food:
                result_name = next(iter(result.keys()))
        result = sod.predict(image)
        mask = visualize_mask(image, result)
        if not mask or not food:
            return FileResponse(f"api/{IMAGE_FOLDER}/{NOT_FOUND_IMAGE}")
        elif mask:
            # result_image = visualize_results(image, result)
            date = datetime.now().strftime("%d-%m-%y_%H-%M-%S")
            filename = f"api/{IMAGE_FOLDER}/{date}_original.jpg"
            result = f"api/{IMAGE_FOLDER}/{date}_{result_name}.jpg"
            image.save(filename, "JPEG")
            mask.save(result, "JPEG")
            return FileResponse(result)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Following error occurred on server: {e}. Please contact support",
        )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")
