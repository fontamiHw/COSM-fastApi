import socket, json, threading

class Routes:
    def __init__(self, app):
        self.app = app  
        self.init = False
    
    def new_connection(self, connection):
        if not self.init:
            self.setup_routes()
            self.init = True
        self.conn = connection
        
    def setup_routes(self):
        @self.app.get("/predict")            
        async def predict(x: float):
            k=1000
            if self.conn:
                k=4
                y = x*k
                return {"result": y}     