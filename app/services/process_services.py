from io import BytesIO

from bson import ObjectId
from fastapi import HTTPException
from models import FileDocument
from services.preprocess import (extract_text_from_csv, extract_text_from_docx,
                                extract_text_from_pdf, extract_text_from_xlsx)
from utils.logger import logger


async def convert_file_to_text(file_content: bytes, filename: str, user_id: str, chat_model: str):
    file_extension = filename.rsplit('.', 1)[-1].lower()
    file_bytes = BytesIO(file_content)

    try:
        content_handlers = {
            'pdf': extract_text_from_pdf,
            'docx': extract_text_from_docx,
            'csv': extract_text_from_csv,
            'xlsx': extract_text_from_xlsx
        }
        if file_extension in content_handlers:
            contents, token_image = await content_handlers[file_extension](file_bytes, user_id, chat_model) if file_extension in ['pdf', 'docx'] else content_handlers[file_extension](file_bytes)
            text = ''.join(content["text"] for content in contents if content["type"] == "text")
            return contents, text, token_image
        else: 
            return None, None, None

    except Exception as e:
        logger.error(f"An error occurred while processing the file: {e}")
        raise HTTPException(status_code=500, detail="Failed to process file")
    

async def insert_document_file_mongo(
    name: str, 
    content: str, 
    token: str, 
    ai_id: str, 
    user_id: str
) -> ObjectId:
    try:
        document = FileDocument(
            name=name,
            content=content,
            token=token,
            userId=ObjectId(user_id),
            aiId=ObjectId(ai_id)
        )
        await document.insert()
        logger.info(f"[USER:{user_id}] Document '{name}' inserted with ID: {document.id}")
        return document.id
    
    except Exception as e:
        logger.error(f"[USER:{user_id}] [AI:{ai_id}] Failed to insert document '{name}': {e}")
        raise HTTPException(status_code=500, detail="Failed to insert document")


# async def search_ais_by_id(ai_id: str) -> AIDocument:
#     ai_document = await AIDocument.find_one(AIDocument.id == ObjectId(ai_id))
#     if ai_document is None:
#         raise HTTPException(status_code=404, detail="Document not found")
#     return ai_document