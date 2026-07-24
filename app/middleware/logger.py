import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start_time = time.perf_counter()

        try:
            response = await call_next(request)

        except Exception:
            logger.exception(
                "Unhandled exception | %s %s | ip=%s",
                request.method,
                request.url.path,
                request.client.host,
            )
            raise

        process_time = (time.perf_counter() - start_time) * 1000

        logger.info(
            "ip=%s | %s %s | status=%d | %.2f ms",
            request.client.host,
            request.method,
            request.url.path,
            response.status_code,
            process_time,
        )

        return response