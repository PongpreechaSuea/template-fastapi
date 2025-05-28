from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class DisableTrailingSlashRedirect(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        """
        Processes an incoming HTTP request to remove a trailing slash from the URL path,
        if present, before passing control to the next middleware or request handler.

        Args:
            request (Request): The incoming HTTP request object.
            call_next (Callable): A function that sends the request to the next middleware
                or request handler.

        Returns:
            Response: The HTTP response from the next middleware or request handler.
        """

        original_path = request.url.path
        if original_path != "/" and original_path.endswith("/"):
            request.scope["path"] = original_path.rstrip("/")
        response = await call_next(request)
        return response