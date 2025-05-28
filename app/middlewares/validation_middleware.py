import re
from typing import List

from configs import config
from fastapi import HTTPException, UploadFile
from utils.logger import logger


def validate_ids(ai_id: str, user_id: str):
    """
    Validate the provided ai_id and user_id to ensure they are not None 
    and match the expected format of a 24-character hexadecimal string.

    Args:
        ai_id (str): The ID of the AI, expected to be a 24-character hexadecimal string.
        user_id (str): The ID of the user, expected to be a 24-character hexadecimal string.

    Raises:
        HTTPException: If ai_id or user_id is None or does not match the expected format.
    """

    if ai_id is None or user_id is None:
        logger.error("ai_id and user_id are required")
        raise HTTPException(status_code=400, detail="ai_id and user_id are required")
    
    if not re.match(config.OBJECT_ID_PATTERN, ai_id):
        logger.error("Invalid ai_id format. Must be 24 characters of hexadecimal")
        raise HTTPException(status_code=400, detail="Invalid ai_id format. Must be 24 characters of hexadecimal")
    
    if not re.match(config.OBJECT_ID_PATTERN, user_id):
        logger.error("Invalid user_id format. Must be 24 characters of hexadecimal")
        raise HTTPException(status_code=400, detail="Invalid user_id format. Must be 24 characters of hexadecimal")


def validate_file_size(file: UploadFile):
    """
    Validate the size of a file to ensure it does not exceed the maximum file size 
    allowed for upload. If the file size exceeds the maximum, an HTTPException will 
    be raised with a status code of 400 and a detail providing the maximum file size 
    allowed.

    Args:
        file (UploadFile): The file to be validated.

    Raises:
        HTTPException: If the file size exceeds the maximum file size allowed.
    """
    
    if file.size > ( config.MAX_FILE_SIZE * 1024 * 1024 ):
        size_mb = int(file.size / (1024 * 1024))
        logger.error(f"File size exceeds {size_mb}MB > {config.MAX_FILE_SIZE}MB")
        raise HTTPException(status_code=400, detail=f"File size exceeds {config.MAX_FILE_SIZE}MB")
    

def validate_files(files: List[UploadFile], user_id):
    """
    Validate a list of files to ensure the total number of files does not exceed
    the maximum number of files allowed for upload. If the total number of files
    exceeds the maximum, an HTTPException will be raised with a status code of 400
    and a detail providing the maximum number of files allowed.

    Args:
        files (List[UploadFile]): The list of files to be validated.
        user_id (str): The ID of the user, used to log the error message.

    Raises:
        HTTPException: If the total number of files exceeds the maximum number of
            files allowed.
    """
    
    if len(files) > config.MAX_FILE:
        logger.error(f"USER:{user_id}] Cannot upload more than {config.MAX_FILE} files")
        raise HTTPException(status_code=400, detail="You can upload a maximum of {MAX_FILE} files.")
    