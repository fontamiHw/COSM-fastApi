import socket, json, threading

class Routes:
    def __init__(self, app, log):
        self.app = app  
        self.init = False
        self.log = log
    
    def new_connection(self, connection):
        if not self.init:
            self.setup_routes()
            self.init = True
        self.conn = connection
        
    def setup_routes(self):
        self.log.info("prepare all the routse")
        
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