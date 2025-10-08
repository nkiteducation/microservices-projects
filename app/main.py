import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("start...")
    yield
    log.info("stop...")


app = FastAPI(lifespan=lifespan, default_response_class=ORJSONResponse)