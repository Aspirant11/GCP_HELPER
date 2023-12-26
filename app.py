# app.py

from helper import GCP_CS

def upload_file_cloud_storage(arg_file_name, arg_bucket_name):
    # Instantiate GCP_CS with credentials path
    gcp_client = GCP_CS(credentials_path="path/to/your/credentials.json")

    # Specify details for file upload
    source_file_path = arg_file_name
    destination_blob_name = f"path/in/your/bucket/{arg_file_name}"

    # Upload file to Google Cloud Storage
    gcp_client.upload_file(arg_bucket_name, source_file_path, destination_blob_name)

def download_file_cloud_storage(arg_file_name, arg_bucket_name):
    # Instantiate GCP_CS with credentials path
    gcp_client = GCP_CS(credentials_path="path/to/your/credentials.json")

    # Specify details for file download
    source_blob_name = f"path/in/your/bucket/{arg_file_name}"
    destination_file_path = f"path/to/your/local/{arg_file_name}"

    # Download file from Google Cloud Storage
    gcp_client.download_file(arg_bucket_name, source_blob_name, destination_file_path)

# Example usage
upload_file_cloud_storage("example.txt", "your_bucket_name")
download_file_cloud_storage("example.txt", "your_bucket_name")
