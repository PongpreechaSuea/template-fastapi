from io import BytesIO

from configs import config
from fastapi import HTTPException, UploadFile
from PIL import Image
from PIL.Image import Image as PILImage


def resize_image(image: PILImage, new_width: int, new_height: int):
    try:
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        return resized_image
    except Exception as e:
        raise HTTPException(status_code=400, detail={e})
    
def validate_image_format(file_stream: BytesIO):
    try:
        SUPPORTED_FORMATS = {"JPEG", "JPG", "PNG", "GIF", "WEBP"}
        image = Image.open(file_stream)
        if image.format not in SUPPORTED_FORMATS:
            raise HTTPException(status_code=400, detail="Unsupported file format.")
        return image
    except IOError:
        raise HTTPException(status_code=400, detail="Invalid image file.")
    
MAX_IMAGE_SIZE = config.MAX_IMAGE_SIZE * 1024 * 1024

def validate_image_size(image: UploadFile):
    if image.size > MAX_IMAGE_SIZE:
        size_mb = int(image.size / (1024 * 1024))
        max_size_mb = int(MAX_IMAGE_SIZE / (1024 * 1024))
        raise HTTPException(status_code=400, detail=f"Image size exceeds {size_mb}MB > {max_size_mb}MB")