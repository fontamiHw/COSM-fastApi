#!/bin/bash
HOST="/data/COSM-bot"  # write here the path of mounted volume
export APPLOGS="${HOST}/logs"
export RESOURCE_PATH="${HOST}/resources"
export APP_PR_FILES="${HOST}/files"
export SUPERVISOR_LOGS="${APPLOGS}/supervisord"

mkdir -p ${HOST}


mkdir -p ${APPLOGS}
mkdir -p ${RESOURCE_PATH}
mkdir -p ${APP_PR_FILES}
mkdir -p ${SUPERVISOR_LOGS} 

FASTAPI_PORT=8000 #the default write in the yaml file 

echo "docker run -d --network Cosm-net -v /data/COSM-bot:/app/host -p ${FASTAPI_PORT}:${FASTAPI_PORT} --name CosmFastApi cosm-fastapi"
      docker run -d --network Cosm-net -v /data/COSM-bot:/app/host -p ${FASTAPI_PORT}:${FASTAPI_PORT} --name CosmFastApi cosm-fastapi
