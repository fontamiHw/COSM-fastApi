#!/bin/bash
export APPLOGS="./host/logs"
export RESOURCE_PATH="./host/resources"
export PYTHONPATH="./src":${PYTHONPATH}


# Path to the YAML file
yaml_file="${RESOURCE_PATH}/fastapi-config.yaml"

# Use yq to extract the value of 'port'
PORT=$(yq eval '.fastapi.port' "$yaml_file")
HOST=$(yq eval '.fastapi.host' "$yaml_file")

fastapi dev src/main.py --host ${HOST} --port ${PORT}
