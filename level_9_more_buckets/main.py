from data_generator import generate_posts
from bucket_manager import create_bucket, upload_blob
from env import get_bucket_name
from logger import logger

def main():
    try:
        # bucket generation
        logger.info(f"Starting main level9")
        bucket_name = get_bucket_name()
        logger.info(f"Creating bucket {bucket_name}")
        bucket = create_bucket(bucket_name)
        logger.info(f"Bucket {bucket_name} created")
        logger.info(f"generating posts")
        posts = generate_posts(20,5)
        logger.info(f"finished generating posts")


        logger.info(f"uploading posts to bucket {bucket_name}")
        for i,post in enumerate(posts):
            post_name = f"post_{i}.txt"
            upload_blob(post,post_name,bucket,is_file=False)
    except Exception as e:
        logger.error(f"An error occured: {str(e)}")


if __name__ == '__main__': 
    main()