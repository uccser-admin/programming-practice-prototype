#!/bin/bash

source ./infrastructure/prod-deploy/load-prod-deploy-config-envs.sh

# Updates the database for the development system
cp ./infrastructure/cloud-sql-proxy/docker-compose.yml ./docker-compose.yml

# Decrypt secret files archive that contain credentials.
./infrastructure/prod-deploy/decrypt-prod-secrets.sh

# Load environment variables.
source ./codewof/load-prod-envs.sh

# Start the system and run the migrate and collect_static system commands.
./dev start
./dev migrate
./dev load_questions
