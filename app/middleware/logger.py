import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start_time = time.time()

        try:

            response = await call_next(request)

        except Exception:

            logger.exception(
                "Unhandled request error"
            )

            raise


        process_time = round(
            (time.time() - start_time) * 1000,
            2
        )


        logger.info(
            "%s %s | status=%s | time=%sms | ip=%s",
            request.method,
            request.url.path,
            response.status_code,
            process_time,
            request.client.host
        )


        return response