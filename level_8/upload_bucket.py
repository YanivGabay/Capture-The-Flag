from google.cloud import storage
from env import get_bucket_name, get_google_cred
from logger import logger

def upload_blob(source_file_name, dest_blob_name):
    try:
        bucket_name = get_bucket_name()
        storage_client = storage.Client.from_service_account_json(get_google_cred())
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(dest_blob_name)

        blob.upload_from_filename(source_file_name)

        logger.critical(f"File {source_file_name} uploaded to {dest_blob_name}.")
    except Exception as e:
        logger.error(f"Failed to upload {source_file_name} to {dest_blob_name}: {str(e)}")

if __name__ == '__main__':
    source_file_name = 'file.txt'
    dest_blob_name = 'file.txt'
    upload_blob(source_file_name, dest_blob_name)
