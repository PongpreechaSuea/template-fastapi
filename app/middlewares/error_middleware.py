from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from utils.logger import logger

async def exception_handler(request: Request, exc: Exception):
    """
    Handles exceptions occurring within the application, logging the error
    and returning an appropriate JSON response.

    Args:
        request (Request): The incoming HTTP request object.
        exc (Exception): The exception that occurred.

    Returns:
        JSONResponse: A JSON response with the appropriate status code and
        error detail. Returns the status code and detail from an HTTPException
        if raised, otherwise returns a 500 Internal Server Error response.
    """

    logger.error(f"Error at {request.method} {request.url.path}: {exc}")
    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )
    
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )
