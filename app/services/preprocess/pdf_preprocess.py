import base64
from io import BytesIO

import fitz
from PIL import Image


async def extract_text_from_pdf(pdf_path: BytesIO, user_id: str, chat_model: str):
    content = ""
    token_image = 0
    data = []

    pdf_document = fitz.open(stream=pdf_path, filetype="pdf")

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)

        text = page.get_text("text")
        if text:
            content += text

        images = page.get_images(full=True)
        if images:
            data.append({
                "type": "text",
                "text": content
            })

            for img_index, img in enumerate(images, start=1):
                image_url, token = await process_image(pdf_document, img, page_num, img_index, user_id, chat_model)
                token_image += token
                data.append({
                    "type": "image_url",
                    "image_url": image_url
                })
            content = ""

    if content:
        data.append({
            "type": "text",
            "text": content
        })

    return data, token_image


async def process_image(pdf_document, img, page_num, img_index, user_id, chat_model):
    from services import calculate_image_token, upload_file_to_s3
    from services.preprocess import resize_image
    xref = img[0]
    base_image = pdf_document.extract_image(xref)
    image_bytes = base_image["image"]

    image_stream = BytesIO(image_bytes)
    image = Image.open(image_stream)

    new_width, new_height, token = calculate_image_token(
        image.width, image.height, chat_model
    )

    resized_img = resize_image(image, new_width, new_height)

    resized_stream = BytesIO()
    resized_img.save(resized_stream, format=image.format)
    resized_stream.seek(0)

    if chat_model == EChatModel.AZURE:
        image_name = f"image_{page_num + 1}_{img_index}.png"
        return await upload_file_to_s3(image_bytes, image_name, user_id), token
    elif chat_model == EChatModel.AWS:
        return f"data:image/png;base64,{base64.b64encode(image_bytes).decode('utf-8')}", token