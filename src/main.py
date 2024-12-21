import os, time, yaml
import threading
import uvicorn

from fastapi import FastAPI
from fastapi_bridge.fastapiServer  import WebServer

# Load configuration from YAML file
# Check if the directory exists, if not, create it
path = os.environ['PYTHONPATH']
print(f"PYTHONPATH {path}")
directory_path = f"{os.environ['RESOURCE_PATH']}/fastapt-config.yaml"       

with open(f"{directory_path}", 'r') as file:
    config = yaml.safe_load(file)
                
app = FastAPI()
webServer = WebServer(app, config)

if __name__ == "__main__":
    uvicorn.run(app)