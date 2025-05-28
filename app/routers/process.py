from typing import List, Optional

from controllers import handle_upload_file
from fastapi import APIRouter, File, Form, UploadFile
from middlewares import validate_files, validate_ids

router = APIRouter(
    prefix="/v1",
    tags=["Process"]
)

@router.post("/process")
async def upload_file(
    files: List[UploadFile] = File(... , alias="file"),
    ai_id: Optional[str] = Form(None, alias="aiId"),
    user_id: Optional[str] = Form(None, alias="userId")
):
    validate_ids(ai_id, user_id)
    validate_files(files, user_id)

    return await handle_upload_file(files, ai_id, user_id)
