#!/bin/bash

# Check if the number of arguments is exactly 2
if [ $# -eq 1 ]; then
#  docker volume create --driver local --opt type=none --opt device=$1 --opt o=bind $2
#  docker run --mount type=volume,src=$2,dst=/app/resources --name CosmBot cosm-bot
  docker run -v $1:/app/host -e FASTAPI_HOST="127.0.0.1" --network host -e FASTAPI_PORT="8000" -p 8000:8000 --name CosmFastApi cosm-fastapi
else
  echo
  echo "------------------------------------------------------------------"
  echo "Incorrect number of arguments."
  echo "The mount volume where there is the CosmFastapi-config.yaml file is mandatory."
  echo "------------------------------------------------------------------"
  echo
fi
