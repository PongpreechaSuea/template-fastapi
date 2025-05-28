from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from utils.logger import logger
from configs import config

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        """
        Middleware to check Authorization header on incoming requests

        If the header is not present or invalid, a 401 Unauthorized response is returned.
        If the header is valid, the request is passed to the next middleware/handler.

        There are some static paths that are excluded from the check: /docs, /openapi.json,
        /swagger-ui.css, /swagger-ui-bundle.js, /swagger-ui-standalone-preset.js, /favicon.ico
        """
        
        STATIC_PATHS = [
            "/docs", "/openapi.json",
            "/swagger-ui.css", "/swagger-ui-bundle.js",
            "/swagger-ui-standalone-preset.js", "/favicon.ico"
        ]
        if request.url.path in STATIC_PATHS:
            return await call_next(request)

        logger.info(f"Authorization Header: {request.headers.get('Authorization')}")

        token = request.headers.get("Authorization")

        print(token, config.AUTH_TOKEN)
        if not token:
            logger.warning("Unauthorized access attempt detected (No Token)")
            raise HTTPException(status_code=401, detail="Unauthorized")

        if token != f"Bearer {config.AUTH_TOKEN}":
            logger.warning(f"Invalid Token: {token}")
            raise HTTPException(status_code=401, detail="Invalid token")

        logger.info("Authorized request")
        return await call_next(request)


