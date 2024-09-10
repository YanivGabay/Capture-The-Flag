
from google.cloud import storage
from env import get_bucket_name, get_google_cred
from logger import logger
import json

def create_bucket(bucket_name):

    storage_client = storage.Client.from_service_account_json(get_google_cred())
    try:
        if storage_client.lookup_bucket(bucket_name):
            logger.critical(f"bucket {bucket_name} already exists")
            return storage_client.get_bucket(bucket_name)
        
        bucket = storage_client.create_bucket(bucket_name)
        logger.critical(f"created bucket {bucket_name}")
        return bucket
    except Exception as e:
        
        logger.critical(f"failed to create bucket: {str(e)}")
        raise e
    

def connect_to_exist_bucket(bucket_name):
    storage_client = storage.Client.from_service_account_json(get_google_cred())
    try:
        bucket = storage_client.get_bucket(bucket_name)
        logger.critical(f"connected to bucket {bucket_name}")
        return bucket
    except Exception as e:
        
        logger.critical(f"failed to connect to bucket: {str(e)}")
        raise e
# upload_blob function
## we can upload from a file or string

def upload_blob(source, dest_blob_name ,curr_bucket ,is_file=True,):
    try:
        bucket = curr_bucket
        blob = bucket.blob(dest_blob_name)

        if is_file:
            blob.upload_from_filename(source)
        else:
            if type(source) == dict:
                source = json.dumps(source)
            blob.upload_from_string(source)

        logger.critical(f"File {source} uploaded to {dest_blob_name}.")
    except Exception as e:
        logger.error(f"Failed to upload {source} to {dest_blob_name}: {str(e)}")


