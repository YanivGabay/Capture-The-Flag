#!/bin/bash

# Configurations Variables
GITHUB_USERNAME="YanivGabay"
IMAGE_NAME="flag-extractor"
TAG="latest"
REMOTE_TAG="ghcr.io/${GITHUB_USERNAME}/${IMAGE_NAME}:${TAG}"
GCE_INSTANCE = 
DOCKER_COMPOSE_FILE="docker-compose.yml"
GITHUB_PAT= 