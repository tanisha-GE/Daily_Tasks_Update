import logging
import time

from fastapi import Request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"

)

logger=logging.getLogger(__name__)

async def logging_middleware(request: Request, call_next):
    start_time=time.time()
    logger.info(
          f"Request started: {request.method} {request.url.path}"
    )

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        f"Request completed: {request.method} "
        f"{request.url.path} - Status: {response.status_code} "
        f"- Time: {process_time:.4f}s"
    )

    return response