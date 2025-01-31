#!/bin/bash
HOST_PATH="/data/COSM-bot"
export APPLOGS="${HOST_PATH}/logs"
export RESOURCE_PATH="${HOST_PATH}/resources"
export APP_PR_FILES="${HOST_PATH}/pr"
export SUPERVISOR_LOGS="${APPLOGS}/supervisord"

mkdir -p ${HOST_PATH}

mkdir -p ${APPLOGS}
mkdir -p ${RESOURCE_PATH}
mkdir -p ${APP_PR_FILES}
mkdir -p ${SUPERVISOR_LOGS}

cp ../CosmFastapi-config.yaml ${RESOURCE_PATH}/CosmFastapi-config.yaml

# Use yq to extract the value of 'port'
FASTAPI_PORT="8000"
FASTAPI_HOST="CosmFastApi.Cosm-net"
CONTAINERCOMM_PORT="5000" 

echo "docker run -d --network Cosm-net -v ${HOST_PATH}:/app/host -p ${FASTAPI_PORT}:${FASTAPI_PORT} -p ${CONTAINERCOMM_PORT}:${CONTAINERCOMM_PORT} --name CosmFastApi cosm-fastapi"
      docker run -d --network Cosm-net -v ${HOST_PATH}:/app/host -p ${FASTAPI_PORT}:${FASTAPI_PORT} -p ${CONTAINERCOMM_PORT}:${CONTAINERCOMM_PORT} --name CosmFastApi cosm-fastapi
