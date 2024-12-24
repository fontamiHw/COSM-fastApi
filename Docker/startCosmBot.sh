#!/bin/bash

 docker run --network host -v /home/civico129/MyProject/COSM-fastApi/host:/app/host -e FASTAPI_HOST="127.0.0.1" -e FASTAPI_PORT="8000" -p 8000:8000 --name CosmFastApi cosm-fastapi

