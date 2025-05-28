import asyncio
import json
import re
from typing import Dict, List

from configs import config
from fastapi import HTTPException, UploadFile
from services import convert_file_to_text, insert_document_file_mongo
from starlette.responses import StreamingResponse
from utils.logger import logger
from utils.token_counter import count_tokens


async def handle_upload_file(files: List[UploadFile], ai_id: str, user_id: str) -> StreamingResponse:
    file_contents = await read_and_store_file_content(files)
    tasks = []
    valid_document_ids = []

    async def process_file():
        for filename, (content, size) in file_contents.items():
            if size > config.MAX_FILE_SIZE * 1024 * 1024:
                yield f"data: Unable to upload : {filename}\n\n"
                continue
            task = process_and_upload_file(filename, content, ai_id, user_id)
            tasks.append(task)

        document_ids = await asyncio.gather(*tasks)
        for message in document_ids:
            if message:
                if re.match(config.OBJECT_ID_PATTERN, message):
                    valid_document_ids.append(message)
                else:
                    yield f"data: {message}\n\n"
                
        yield f"data: {json.dumps({'document_ids': valid_document_ids})}\n\n"

    return StreamingResponse(process_file(), media_type='text/event-stream')


async def read_and_store_file_content(files: List[UploadFile]) -> Dict[str, tuple]:
    file_contents = {}
    for file in files:
        try:
            content = await file.read()
            file_contents[file.filename] = (content, file.size)
        except Exception as e:
            logger.error(f"Error reading file {file.filename}: {e}", exc_info=True)
            raise HTTPException(status_code=400, detail="An error occurred uploading. Please try again.")
    return file_contents

async def process_and_upload_file(filename: str, content: bytes, ai_id: str, user_id: str) -> str:
    try:
        data_ais = "AZURE"
        max_token = 50000

        file_content, text, token_image = await convert_file_to_text(content, filename, user_id, data_ais)
        if text is None:
            return f"Unsupported file : {filename}"

        token_count = count_tokens(text, 'o200k_base')
        if token_count > max_token:
            return f"Unable to upload : {filename}"

        document_id = await insert_document_file_mongo(
            name=filename,
            content=file_content,
            token=(token_count+token_image),
            ai_id=ai_id,
            user_id=user_id,
        )
        return str(document_id)
    except Exception as e:
        logger.error(f"Error processing file {filename}: {e}", exc_info=True)
        return "An error occurred uploading. Please try again."

