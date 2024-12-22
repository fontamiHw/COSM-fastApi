import os, time, yaml
import threading
import uvicorn
import logger

from fastapi import FastAPI
from fastapi_bridge.fastapiServer  import WebServer
from contextlib import asynccontextmanager

# Load configuration from YAML file
# Check if the directory exists, if not, create it
path = os.environ['PYTHONPATH']
directory_path = f"{os.environ['RESOURCE_PATH']}/CosmFastapi-config.yaml"       
log = logger.getLogger()

with open(f"{directory_path}", 'r') as file:
    config = yaml.safe_load(file)
                
@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("fastApi starting.... create server socket")      
    webServer = WebServer(app, config, log)
    yield
    log.info("fastApi closing.... close all open socket")      
    webServer.close_all()
                
app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app)