import fitz
import json
import os

pdf_path = "./pdf/เอกสารสำหรับการอนุมัติโครงการ 1.pdf"
output_folder = "./output_images"
content = ""
data = []

os.makedirs(output_folder, exist_ok=True)

pdf_document = fitz.open(pdf_path)
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    text = page.get_text("text")
    images = page.get_images(full=True)

    if text:
        content += text
    
    if images:
        data.append({
            "type": "text",
            "text": content
        })
        for img_index, img in enumerate(images, start=1):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]

            print(image_bytes)
            image_filename = f"image_{page_num + 1}_{img_index}.png"
            image_path = os.path.join(output_folder, image_filename)

            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)

            data.append({
                "type": "image_url",
                "image_url": image_path
            })
        content = ""
if content:
    data.append({
        "type": "text",
        "text": content
    })

json_data = json.dumps(data, indent=4, ensure_ascii=False)
print(json_data)
