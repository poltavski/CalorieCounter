from PIL import Image, ImageOps


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
