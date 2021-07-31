from PIL import Image, ImageOps
from api.settings import (
    DETALIZATION,
    INFERENCE_THRESHOLD,
    IMAGE_FOLDER,
    NOT_FOUND_IMAGE,
    RESULT_NAME,
)
from datetime import datetime


def label_processing(image, food_classifier, percentage):
    result = food_classifier.predict(image)
    if percentage:
        for key, value in result.items():
            result[key] = f"{round(value * 100)}%"
    return result


def mask_processing(image, sod, food_classifier, food_restriction):
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
    mask = visualize_mask(image, result)
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
        print(result)
        return result


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
