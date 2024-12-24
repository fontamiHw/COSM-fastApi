#!/bin/bash

echo "move resource files int the mounted path"
# Variables for source and destination directories
source_file=${TMP_RESOURCE_PATH}/CosmFastapi-config.yaml
destination_dir=${RESOURCE_PATH}

# Extract the filename from the source file path
filename="CosmFastapi-config.yaml"

# Check if the file already exists in the destination directory
if [ ! -e "$destination_dir/$filename" ]; then
    # Copy the file to the destination directory
    cp "$source_file" "$destination_dir/"
    echo "File '$filename' copied to '$destination_dir'."
else
    echo "File '$filename' already exists in '$destination_dir'. No action taken."
fi
echo
echo "show mounted volume"
ls -latR /app/host
echo


export PATH="$APP_COSM_PATH:$PATH"
echo "show enviroment variable"
env

echo "moving in /app/CosmFastApi"
cd /app/CosmFastApi
pwd


########### START APPLICATION ###########
echo "Cosm fastapi Starting on --host ${FASTAPI_HOST} --port ${FASTAPI_PORT} ....."
fastapi run main.py --host ${FASTAPI_HOST} --port ${FASTAPI_PORT}
