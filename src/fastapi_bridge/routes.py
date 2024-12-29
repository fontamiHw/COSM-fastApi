import os, json
import logger
from fastapi_bridge.model.routeModels import PrItem
from fastapi import File, HTTPException, UploadFile

    
class Routes:
    def __init__(self, app):
        self.app = app  
        self.init = False
        self.log = logger.getLogger("Routes")
        self.directory_path = f"{os.environ['APP_PR_FILES']}"       

    
    def new_connection(self, connection):
        if not self.init:
            self.setup_routes()
            self.init = True
        self.conn = connection
        
    def setup_routes(self):        
        self.log.info("prepare all the routes")
        
        @self.app.post('/pr')
        async def receive_json(item: PrItem):
            item.command ='pr'
            item_dict = item.model_dump()
            self.log.info(f"received from path /pr : {item_dict}")
            self.send(item_dict)
            return {"message": "command processed"}

        @self.app.post('/pr/file')
        def upload(file: UploadFile = File(...)):
            item_dict = {'command': 'prFile', 'filename': file.filename}        
            self.log.info(f"received from path /pr/file : {item_dict}")
            try:
                contents = file.file.read()
                with open(f"{self.directory_path}/{file.filename}", 'wb') as f:
                    f.write(contents)
            except Exception:
                raise HTTPException(status_code=500, detail='Something went wrong')
            finally:
                file.file.close()

            return {"message": f"Successfully uploaded {file.filename}"}
                
        @self.app.get("/predict")            
        async def predict(x: float):
            self.log.info(f" Invoked /predict with x={x}")
            k=1000
            if self.conn:
                k=4
                y = x*k
                data =  {"result": y}
                self.send(data)
                return data     
    
    def send(self, data):
        self.log.info(f"Sending {data}")
        jsonDump = json.dumps(data)
        dataB = bytes(jsonDump, encoding="utf-8")
        self.conn.send(dataB)  # send data to the client
        


