import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.NODE_ENV = os.getenv("NODE_ENV", "dev")
        self.HOST = str(os.getenv("HOST", "0.0.0.0"))
        self.PORT = int(os.getenv("PORT", 8000))
        self.VERSION = str(os.getenv("VERSION", "1.0.0"))
        self.SERVICE_NAME = str(os.getenv("SERVICE_NAME", "Template FastAPI"))

        self.AUTH_TOKEN = str(os.getenv("AUTH_TOKEN", None))

        self.MONGO_URL = str(os.getenv("MONGO_URL", None))

        self.S3_AWS_ACCESS_KEY = str(os.getenv("S3_AWS_ACCESS_KEY", None))
        self.S3_AWS_SECRET_ACCESS_KEY = str(os.getenv("S3_AWS_SECRET_ACCESS_KEY", None))
        self.S3_AWS_BUCKET = str(os.getenv("S3_AWS_BUCKET", None))
        self.S3_AWS_EXPIRES_IN = int(os.getenv("S3_AWS_EXPIRES_IN", 60))

        self.MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 10))
        self.MAX_IMAGE_SIZE = int(os.getenv("MAX_IMAGE_SIZE", 20))
        self.MAX_FILE = int(os.getenv("MAX_FILE", 10))
        self.PATH_S3_FOLDER_FILE = str(os.getenv("PATH_S3_FOLDER_FILE", None))
        self.OBJECT_ID_PATTERN = r"^[a-f0-9]{24}$"
        self.RETRY_DELAY = int(os.getenv("RETRY_DELAY", 5))


    def show_all(self):
        for attr, value in self.__dict__.items():
            print(f"{attr} = {value}")

config = Config()