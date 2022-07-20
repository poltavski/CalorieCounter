from PIL import Image, ImageOps, ImageDraw
from typing import Dict
import cv2
import numpy as np

from api.settings import (
    DETALIZATION,
    INFERENCE_THRESHOLD,
    IMAGE_FOLDER,
    NOT_FOUND_IMAGE,
    RESULT_NAME,
    FOOD_101_MAPPING
)
from datetime import datetime
from database.database import get_db
from database.models import FoodModel


def label_processing(image, food_classifier, percentage):
    result = food_classifier.predict(image)
    if percentage:
        for key, value in result.items():
            result[key] = f"{round(value * 100)}%"
    return result


def mask_processing(image, sod, food_classifier, food_restriction, resize_result, resize_width, resize_height):
    food = not food_restriction
    result_name = RESULT_NAME
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

    mask = visualize_mask(
        image, result,
        resize=resize_result,
        width=resize_width,
        height=resize_height
    )

    if not mask or not food:
        return f"{IMAGE_FOLDER}/{NOT_FOUND_IMAGE}"
    elif mask:
        # result_image = visualize_results(image, result)
        date = datetime.now().strftime("%d-%m-%y_%H-%M-%S")
        result = f"{IMAGE_FOLDER}/{date}_{result_name}.jpg"
        if DETALIZATION == 1:
            filename = f"{IMAGE_FOLDER}/{date}_original.jpg"
            image.save(filename, "JPEG")
            mask.save(result, "JPEG")
        return result


def visualize_mask(
        orig_image, pred_image, resize: bool = False, width: int = 0, height: int = 0
):
    """Visualize mask on image. Resize by option

    Args:
        orig_image:
        pred_image:
        resize:
        width:
        height:

    Returns:
        Image with mask
    """
    mask = Image.new("L", orig_image.size, 128)
    pred_image = ImageOps.colorize(
        pred_image.convert("L"), black="black", white="green"
    )

    pred_image = pred_image.resize(orig_image.size)
    mask_area, image_ratio = get_mask_area(pred_image)
    result = Image.composite(orig_image, pred_image, mask)

    if resize:
        if width and height:
            new_size = (width, height)
            result = result.resize(new_size, Image.ANTIALIAS)
        elif width:
            new_size = (width, int(width / image_ratio))
            result = result.resize(new_size, Image.ANTIALIAS)
        elif height:
            new_size = (int(height * image_ratio), height)
            result = result.resize(new_size, Image.ANTIALIAS)

    ImageDraw.Draw(
        result  # Image
    ).text(
        (10, 10),  # Coordinates
        f"Recognized object area: {mask_area}% of image. (c) Calorie Counter",  # Text
        (0, 0, 0)  # Color
    )
    return result


def get_mask_area(mask):
    """Get mask area and size ratio."""
    n = np.array(mask)
    # Mask of green background pixels
    bgMask = (n[:, :, 0:3] == [0, 0, 0]).all(2)
    total_pixels = mask.width * mask.height
    ratio = mask.width / mask.height
    object_pixels = total_pixels - np.count_nonzero(bgMask)
    mask_area = round(object_pixels / total_pixels, 3) * 100
    return mask_area, ratio


def get_food_table(food_category: str = None, page: int = 1, num_records: int = 100) -> dict:
    """Get food_nutrient table data."""
    get_db()
    if food_category is not None:
        where_criteria = FOOD_101_MAPPING.get(food_category)
        if where_criteria:
            query = FoodModel.select().where(FoodModel.id.in_(where_criteria))
    else:
        query = FoodModel.select()
    # .paginate(page, num_records)
    data = [[
        # item.id,
        item.food_group,
        item.name,
        item.calories,
        item.protein_g,
        item.fat_g,
        item.carbs_g,
        item.sugars_g,
        item.moisture_g,
        item.energy_with_dietary_fibre_kj,
        item.energy_without_dietary_fibre_kj,
    ] for item in query]
    return data
