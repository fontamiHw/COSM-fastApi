#!/bin/bash

export RESOURCE_PATH="host/resources"
# Path to the YAML file
yaml_file="${RESOURCE_PATH}/CosmFastapi-config.yaml"

# Use yq to extract the value of 'port'
FASTAPI_PORT=$(yq eval '.fastapi.port' "$yaml_file")
FASTAPI_HOST=$(yq eval '.fastapi.host' "$yaml_file")

echo "docker run --network Cosm-net --ip ${FASTAPI_HOST} -v /home/civico129/MyProject/COSM-fastApi/host:/app/host -e FASTAPI_HOST=${FASTAPI_HOST} -e FASTAPI_PORT=${FASTAPI_PORT} -p 8000:8000 --name CosmFastApi cosm-fastapi"
      docker run --network Cosm-net --ip ${FASTAPI_HOST} -v /home/civico129/MyProject/COSM-fastApi/host:/app/host -e FASTAPI_HOST=${FASTAPI_HOST} -e FASTAPI_PORT=${FASTAPI_PORT} -p 8000:8000 --name CosmFastApi cosm-fastapi

# echo 'docker run -v /home/civico129/MyProject/COSM-fastApi/host:/app/host -e FASTAPI_HOST="127.0.0.1" -e FASTAPI_PORT="8000" --name CosmFastApi cosm-fastapi'
# docker run -v /home/civico129/MyProject/COSM-fastApi/host:/app/host -e FASTAPI_HOST="192.168.1.75" -e FASTAPI_PORT="8000" --name CosmFastApi cosm-fastapi