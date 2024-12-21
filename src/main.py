import os, time, yaml
import threading
import uvicorn

from fastapi import FastAPI
from fastapi_bridge.fastapiServer  import WebServer
from contextlib import asynccontextmanager

# Load configuration from YAML file
# Check if the directory exists, if not, create it
path = os.environ['PYTHONPATH']
directory_path = f"{os.environ['RESOURCE_PATH']}/fastapi-config.yaml"       

with open(f"{directory_path}", 'r') as file:
    config = yaml.safe_load(file)
                
@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"\n\n\n\nlifespan started   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n")      
    webServer = WebServer(app, config)
    yield
    webServer.close_all()
    print(f"\n\n\n\nlifespan completed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n")  
                
app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app)