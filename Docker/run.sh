#!/bin/bash

source ./.enviroment
echo "show enviroment variable"
env
echo
echo "show mounted volume"
ls -latR /app/host
echo

echo "moving in /app/CosmFastApi"
cd /app/CosmFastApi
pwd

echo "python version is"
python --version



########### START APPLICATION ###########

# # Path to the YAML file
# yaml_file="${RESOURCE_PATH}/CosmFastapi-config.yaml"
# cat ${yaml_file}
# # Use yq to extract the value of 'port' and 'host'
# echo "read config file ${yaml_file}."
# PORT=$(yq eval '.fastapi.port' "${yaml_file}")
# HOST=$(yq eval '.fastapi.host' "${yaml_file}")

echo "Cosm fastapi Starting on --host ${FASTAPI_HOST} --port ${FASTAPI_PORT} ....."
fastapi run main.py --host ${FASTAPI_HOST} --port ${FASTAPI_PORT}
