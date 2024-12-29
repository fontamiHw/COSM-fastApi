#!/bin/bash
HOST="../host"
export APPLOGS="${HOST}/logs"
export RESOURCE_PATH="${HOST}/resources"
export APP_PR_FILES="${HOST}/pr"

mkdir -p ${APPLOGS}
mkdir -p ${RESOURCE_PATH}
mkdir -p ${APP_PR_FILES}
rm -rf ${APPLOGS}/*
rm -rf ${RESOURCE_PATH}/*
rm -rf ${APP_PR_FILES}/*

cp ../CosmFastapi-config.yaml ${RESOURCE_PATH}/CosmFastapi-config.yaml

# Path to the YAML file
yaml_file="${RESOURCE_PATH}/CosmFastapi-config.yaml"

# Use yq to extract the value of 'port'
FASTAPI_PORT=$(yq eval '.fastapi.port' "$yaml_file")
FASTAPI_HOST=$(yq eval '.fastapi.host' "$yaml_file")
CONTAINERCOMM_PORT=$(yq eval '.container_communication.port' "$yaml_file")

echo "docker run --network Cosm-net --ip ${FASTAPI_HOST} -v /home/civico129/MyProject/COSM-fastApi/host:/app/host -e FASTAPI_HOST=${FASTAPI_HOST} -e FASTAPI_PORT=${FASTAPI_PORT} -p ${FASTAPI_PORT}:${FASTAPI_PORT} --name CosmFastApi cosm-fastapi"
      docker run --network Cosm-net --ip ${FASTAPI_HOST} -v /home/civico129/MyProject/COSM-fastApi/host:/app/host -e FASTAPI_HOST=${FASTAPI_HOST} -e FASTAPI_PORT=${FASTAPI_PORT} -p ${FASTAPI_PORT}:${FASTAPI_PORT} --name CosmFastApi cosm-fastapi
