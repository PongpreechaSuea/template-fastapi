from fastapi import APIRouter, status

router = APIRouter(
    prefix="/v1/health",
    tags=["Health"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def check_status():
    return {"success": True}
