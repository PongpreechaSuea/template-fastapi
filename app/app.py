from contextlib import asynccontextmanager

from configs import config
from connects import MongoClientManager, S3ClientManager
from fastapi import FastAPI
from middlewares import (AuthMiddleware, DisableTrailingSlashRedirect,
                        exception_handler, setup_cors)
from routers import health, process, http


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not await MongoClientManager.is_connected():
        await MongoClientManager.connect()
    S3ClientManager.connect()
    yield

app = FastAPI(
    lifespan=lifespan,
    title=config.SERVICE_NAME,
    version=config.VERSION,
    description=config.SERVICE_NAME,
)

setup_cors(app)
# app.add_middleware(AuthMiddleware)
app.add_middleware(DisableTrailingSlashRedirect)
app.add_exception_handler(Exception, exception_handler)

app.include_router(http.router)
app.include_router(health.router)
app.include_router(process.router)
