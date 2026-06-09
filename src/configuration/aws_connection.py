import boto3
import os
import logging
from src.constants import AWS_SECRET_ACCESS_KEY_ENV_KEY, AWS_ACCESS_KEY_ID_ENV_KEY, REGION_NAME


class S3Client:

    s3_client = None
    s3_resource = None

    def __init__(self, region_name=REGION_NAME):
        """
        Creates S3 connection if AWS credentials exist.
        If not found → disables S3 instead of crashing pipeline.
        """

        try:
            if S3Client.s3_resource is None or S3Client.s3_client is None:

                access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY)
                secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)

                # ✅ SAFE MODE (IMPORTANT FOR RESUME PROJECT)
                if not access_key_id or not secret_access_key:
                    logging.warning(
                        "AWS credentials not found. S3 features will be disabled."
                    )
                    self.s3_client = None
                    self.s3_resource = None
                    return

                S3Client.s3_resource = boto3.resource(
                    "s3",
                    aws_access_key_id=access_key_id,
                    aws_secret_access_key=secret_access_key,
                    region_name=region_name
                )

                S3Client.s3_client = boto3.client(
                    "s3",
                    aws_access_key_id=access_key_id,
                    aws_secret_access_key=secret_access_key,
                    region_name=region_name
                )

            self.s3_resource = S3Client.s3_resource
            self.s3_client = S3Client.s3_client

        except Exception as e:
            logging.error(f"S3 initialization failed: {str(e)}")
            self.s3_client = None
            self.s3_resource = None