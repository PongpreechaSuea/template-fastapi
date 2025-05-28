from configs import config
from fastapi import APIRouter, status

router = APIRouter(
    tags=["Health"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def check_status():
    return {
        "success": True,
        "version": config.VERSION,
        "name": config.SERVICE_NAME
    }
