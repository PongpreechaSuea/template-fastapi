from configs import config
from utils.logger import logger

if __name__ == "__main__":
    logger.info(f"Documentation: http://{config.HOST}:{config.PORT}/docs")
    import uvicorn
    uvicorn.run("app:app", host=config.HOST, port=config.PORT, log_config=None, reload=True)
