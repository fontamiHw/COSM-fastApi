#!/bin/bash
########### PREPARE MOUNTED VOLUME ###########
echo "Creating mounted directories"
mkdir -p ${APPLOGS}
mkdir -p ${RESOURCE_PATH}
mkdir -p ${APP_PR_FILES}

########### PREPARE CONFIG IN MOUNTED VOLUME ###########
echo "move resource files into the mounted path"
filename="CosmFastapi-config.yaml"
# Variables for source and destination directories
source_file=${TMP_RESOURCE_PATH}/${filename}
destination_dir=${RESOURCE_PATH}

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

########### ENVIROMENT ###########
export PATH="$APP_COSM_PATH:$PATH"

echo "integrate the COM_FASTAPI enviromental variable"
# Path to the YAML file
yaml_file="${RESOURCE_PATH}/CosmFastapi-config.yaml"

# Use yq to extract the value of 'port'
export FASTAPI_PORT=$(yq eval '.fastapi.port' "$yaml_file")
export FASTAPI_HOST=$(yq eval '.fastapi.host' "$yaml_file")
export CONTAINERCOMM_PORT=$(yq eval '.container_communication.port' "$yaml_file") 

echo "show enviroment variable"
env
echo

########### START APPLICATION ###########
echo "moving in ${APP_COSM_PATH}"
cd ${APP_COSM_PATH}
pwd
echo "Cosm fastapi Starting on --host ${FASTAPI_HOST} --port ${FASTAPI_PORT} ....."
fastapi run main.py --host ${FASTAPI_HOST} --port ${FASTAPI_PORT}
