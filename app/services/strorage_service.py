# Import boto3 to interact with S3-compatible storage
import boto3

# Import exception handling for storage operations
from botocore.exceptions import ClientError

# Import application configuration
from config import Config


class S3Storage:
    """
    Storage service responsible for interacting
    with MinIO object storage.
    """

    def __init__(self):
        """
        Initialize MinIO client.
        """

        self.s3 = boto3.client(
            "s3",

            # MinIO endpoint
            endpoint_url=Config.MINIO_ENDPOINT,

            # MinIO username
            aws_access_key_id=Config.MINIO_ACCESS_KEY,

            # MinIO password
            aws_secret_access_key=Config.MINIO_SECRET_KEY
        )

        # Bucket name used by the application
        self.bucket = Config.MINIO_BUCKET_NAME

    def upload_file(self, file_obj, filename):
        """
        Upload a file to MinIO.

        Parameters:
            file_obj : Uploaded file object
            filename : Object name inside bucket
        """

        try:

            # Upload file object to bucket
            self.s3.upload_fileobj(
                file_obj,
                self.bucket,
                filename
            )

            return True

        except ClientError as e:

            print(f"Error uploading file: {e}")
            return False

    def get_file(self, filename):
        """
        Retrieve a file from MinIO.

        Parameters:
            filename : File name stored in bucket

        Returns:
            File stream if found
            None if retrieval fails
        """

        try:

            # Retrieve object from bucket
            response = self.s3.get_object(
                Bucket=self.bucket,
                Key=filename
            )

            # Return file content stream
            return response["Body"]

        except ClientError as e:

            print(f"Error retrieving file: {e}")
            return None

