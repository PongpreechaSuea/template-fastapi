import asyncio

import models
from beanie import init_beanie
from configs import config
from motor.motor_asyncio import AsyncIOMotorClient
from utils.logger import logger


class MongoClientManager:
    _client = None
    _db = None
    _retry_delay = config.RETRY_DELAY

    @classmethod
    async def connect(cls):
        if cls._client is None:
            try:
                logger.info("Attempting to connect to MongoDB...")
                cls._client = AsyncIOMotorClient(config.MONGO_URL)

                await cls._client.admin.command('ping')
                cls._db = cls._client.get_default_database()
                await init_beanie(
                    database=cls._db,
                    document_models=models.__all__
                )
                logger.info("MongoDB Connected")
            except Exception as e:
                logger.error(f"MongoDB Connection Failed: {e}")
                logger.info(f"Retrying in {cls._retry_delay} seconds...")
                await asyncio.sleep(cls._retry_delay)

    @classmethod
    async def close(cls):
        if cls._client:
            cls._client.close()
            cls._client = None
            cls._db = None
            logger.info("MongoDB Disconnected")

    @classmethod
    async def is_connected(cls):
        try:
            if cls._client:
                await cls._client.admin.command('ping')
                return True
            return False
        except Exception:
            return False

    @classmethod
    async def get_db(cls):
        if not await cls.is_connected():
            await cls.connect()
        return cls._db

