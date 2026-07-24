from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.services.rate_limit_service import RateLimitService


class RateLimitMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)
        self.rate_limit = RateLimitService()

    async def dispatch(self, request: Request, call_next):

        # Ограничиваем только отправку формы
        if (
            request.method == "POST"
            and request.url.path == "/api/contact"
        ):

            ip = request.client.host

            if not self.rate_limit.is_allowed(ip):

                return JSONResponse(
                    status_code=429,
                    content={
                        "success": False,
                        "message": "Too many requests. Please try again later."
                    }
                )

        response = await call_next(request)

        return response