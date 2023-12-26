# helper.py

from google.cloud import storage

class GCP_CS:
    def __init__(self, credentials_path=None):
        """Initialize Google Cloud Storage client."""
        if credentials_path:
            # Set Google Cloud Storage credentials
            storage.Client.from_service_account_json(credentials_path)

    def upload_file(self, bucket_name, source_file_path, destination_blob_name):
        """Upload a file to Google Cloud Storage bucket."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_path)

        print(f"File {source_file_path} uploaded to {destination_blob_name} in {bucket_name}.")

    def download_file(self, bucket_name, source_blob_name, destination_file_path):
        """Download a file from Google Cloud Storage bucket."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(source_blob_name)

        blob.download_to_filename(destination_file_path)

        print(f"File {source_blob_name} downloaded to {destination_file_path}.")

# Example Usage:
# Instantiate GCP_CS with credentials path
gcp_client = GCP_CS(credentials_path="path/to/your/credentials.json")

# Specify details for file download
bucket_name = "your_bucket_name"
source_blob_name = "path/in/your/bucket/file.txt"
destination_file_path = "path/to/your/local/downloaded_file.txt"

# Download file from Google Cloud Storage
gcp_client.download_file(bucket_name, source_blob_name, destination_file_path)
