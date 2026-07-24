from fastapi import Request
from fastapi.responses import JSONResponse

from app.utils.logger import logger


async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(
        "Exception: %s",
        exc
    )


    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error"
        }
    )