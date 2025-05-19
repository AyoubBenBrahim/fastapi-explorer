#!/bin/bash

# Set project root
ROOT_DIR="fastapi_docker"

# Create directories
mkdir -p $ROOT_DIR/app
mkdir -p $ROOT_DIR/scripts

# Create empty files
touch $ROOT_DIR/app/__init__.py
touch $ROOT_DIR/app/main.py
touch $ROOT_DIR/app/database.py
touch $ROOT_DIR/app/models.py
touch $ROOT_DIR/Dockerfile
touch $ROOT_DIR/docker-compose.yml
touch $ROOT_DIR/requirements.txt
touch $ROOT_DIR/scripts/wait-for-postgres.sh

echo "✅ Project structure 'fastapi_docker/' created."

