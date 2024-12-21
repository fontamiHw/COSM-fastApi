import os, time, yaml
import threading
import uvicorn

from fastapi import FastAPI
from fastapi_bridge.fastapiServer  import WebServer

# Load configuration from YAML file
# Check if the directory exists, if not, create it
path = os.environ['PYTHONPATH']
print(f"PYTHONPATH {path}")
directory_path = f"{os.environ['RESOURCE_PATH']}/config.yaml"       

with open(f"{directory_path}", 'r') as file:
    config = yaml.safe_load(file)
    fastapi_config = config['fastapi']
                
app = FastAPI(host=fastapi_config['host'], port=fastapi_config['port'])
webServer = WebServer(app)

if __name__ == "__main__":
    uvicorn.run(app, host=fastapi_config['host'], port=fastapi_config['port'])