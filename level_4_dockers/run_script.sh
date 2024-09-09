#!/bin/bash

echo "Script has started"

# Load environment variables
source ./.env

# Function to build and push Docker image
build_and_push_image() {
    echo "Building Docker image..."
    docker build -t $IMAGE_NAME:$TAG .

    echo "Tagging image..."
    docker tag $IMAGE_NAME:$TAG $REMOTE_TAG

    echo "Logging into Docker registry..."
    echo $GITHUB_PAT | docker login ghcr.io -u $GITHUB_USERNAME --password-stdin

    echo "Pushing image to registry..."
    docker push $REMOTE_TAG
}

# Function to pull Docker image on GCE
pull_image_on_gce() {
    echo "Pulling image on GCE..."
    ssh -i $SSH_KEY_PATH $GCE_INSTANCE "docker pull $REMOTE_TAG"
}

# Function to copy Docker Compose files to GCE
copy_compose_file_to_gce() {
    echo "Copying Docker Compose file to GCE..."
    scp -i $SSH_KEY_PATH $DOCKER_COMPOSE_FILE_PATH $GCE_INSTANCE:/path/to/destination/
}

# Execute functions
build_and_push_image
pull_image_on_gce
copy_compose_file_to_gce

echo "Automation script completed successfully."
