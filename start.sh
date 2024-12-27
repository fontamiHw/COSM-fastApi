#!/bin/bash
export APPLOGS="./host/logs"
export RESOURCE_PATH="./host/resources"
export PYTHONPATH="./src":${PYTHONPATH}


# Path to the YAML file
yaml_file="${RESOURCE_PATH}/CosmFastapi-config.yaml"

# Use yq to extract the value of 'port'
FASTAPI_PORT=$(yq eval '.fastapi.port' "$yaml_file")
FASTAPI_HOST=$(yq eval '.fastapi.host' "$yaml_file")

fastapi run src/main.py --host ${FASTAPI_HOST} --port ${FASTAPI_PORT}
