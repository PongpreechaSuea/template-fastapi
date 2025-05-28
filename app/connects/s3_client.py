import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from configs import config
from utils.logger import logger

class S3ClientManager:
    _resource = None
    _bucket_name = config.S3_AWS_BUCKET

    @classmethod
    def connect(cls):
        if cls._resource is None:
            try:
                logger.info("Attempting to connect to S3...")
                cls._resource = boto3.resource(
                    's3',
                    aws_access_key_id=config.S3_AWS_ACCESS_KEY,
                    aws_secret_access_key=config.S3_AWS_SECRET_ACCESS_KEY
                )
                logger.info("Connected to S3")
            except NoCredentialsError:
                logger.error("AWS credentials not found")
                raise NoCredentialsError("AWS credentials not found")
            except PartialCredentialsError:
                logger.error("Incomplete AWS credentials")
                raise PartialCredentialsError("Incomplete AWS credentials")
            except Exception as e:
                logger.error(f"Failed to connect to S3: {e}")
                raise ClientError(e.response, e.operation_name)

    @classmethod
    def get_client(cls):
        if cls._resource is None:
            cls.connect()
        return cls._resource

    @classmethod
    def get_bucket_name(cls) -> str:
        return cls._bucket_name

    @classmethod
    def disconnect(cls):
        if cls._resource is not None:
            try:
                cls._resource.meta.client.close()
                cls._resource = None
                logger.info("S3 Disconnected")
            except Exception as e:
                logger.error(f"Failed to disconnect from S3: {e}")
                raise
