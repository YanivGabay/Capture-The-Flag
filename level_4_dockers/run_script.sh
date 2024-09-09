#!/bin/bash

# Abort on any error (equivalent to set -e)
set -e

echo "Script has started"


## because i didnt understand why it isnt working
## i forgot to open the docker daemon on windows
## i created this function to check if the docker daemon is running
ask_docker_status() {
    echo "Is the Docker daemon running? (yes/no)"
    read -r answer  # Read user input into variable 'answer'

    # Normalize input to lowercase to simplify comparison
    answer=$(echo "$answer" | tr '[:upper:]' '[:lower:]')

    if [ "$answer" != "yes" ]; then
        echo "Please start the Docker daemon before running this script."
        exit 1  # Exit if Docker is not running
    fi
}

ask_docker_status

# Load environment variables
if [ ! -f ./.env ]; then #check if file doesnt exists
    echo ".env file not found."
    exit 1
else
    source ./.env
fi




# Function to build and push Docker image
##  just the steps with did previously withing a script
build_and_push_image() {
    echo "Building Docker image..."
    docker build -t $IMAGE_NAME:$TAG . || { echo "Failed to build Docker image"; exit 1; }

    echo "Tagging image..."
    docker tag $IMAGE_NAME:$TAG $REMOTE_TAG || { echo "Failed to tag Docker image"; exit 1; }

    echo "Logging into Docker registry..."
    echo $GITHUB_PAT | docker login ghcr.io -u $GITHUB_USERNAME --password-stdin || { echo "Failed to login to Docker registry"; exit 1; }

    echo "Pushing image to registry..."
    docker push $REMOTE_TAG || { echo "Failed to push Docker image to registry"; exit 1; }
}

# Function to pull Docker image on GCE
# Function to login and pull Docker image on GCE

## this part was the most complex to do
## we basicly feed the ssh command with the script we want to run on the remote machine
## we must not forget to connect to the docker registry before pulling the image inside
## the remote machine
login_and_pull_image_on_gce() {
    echo "Ensuring Docker on GCE is logged in and pulling the image..."
    ssh -i $SSH_KEY_PATH $GCE_INSTANCE <<EOF
        set -e  # Ensure any error leads to termination of the script

        # Login to Docker registry
        echo "Logging into Docker registry..."
        echo $GITHUB_PAT | docker login ghcr.io -u $GITHUB_USERNAME --password-stdin || { echo "Failed to login to Docker registry"; exit 1; }

        # Pull the Docker image
        echo "Pulling Docker image..."
        docker pull $REMOTE_TAG || { echo "Failed to pull Docker image"; exit 1; }

        echo "Docker image pulled successfully."
EOF
    if [ $? -ne 0 ]; then
        echo "Failed to execute operations on GCE"
        exit 1
    fi
}


# Function to copy Docker Compose files to GCE
copy_compose_file_to_gce() {
    echo "Copying Docker Compose file to GCE..."
    scp -i $SSH_KEY_PATH $DOCKER_COMPOSE_FILE_PATH $GCE_INSTANCE:$DOCKER_COMPOSE_FILE_PATH || { echo "Failed to copy Docker Compose file to GCE"; exit 1; }
}

# Execute functions
build_and_push_image
ssh -i $SSH_KEY_PATH $GCE_INSTANCE "echo $GITHUB_PAT | docker login ghcr.io -u $GITHUB_USERNAME --password-stdin && docker pull ghcr.io/yanivgabay/flag-extractor:latest"

login_and_pull_image_on_gce
copy_compose_file_to_gce

echo "Automation script completed successfully."
