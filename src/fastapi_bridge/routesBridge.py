import os, json, time
import logger
from fastapi_bridge.routes.prRoutes import PrRoutes
from fastapi_bridge.routes.debugUsersRoutes import DebugUsersRoutes
from fastapi_bridge.routes.debugServerRoutes import DebugServerRoutes
from fastapi_bridge.routes.debugDataBaseRoutes import DebugDataBaseRoutes
from fastapi_bridge.routes.systemRoutes import SystemRoutes

    
class RoutesBridge(object):
    def __init__(self, app):
        self.app = app  
        self.init = False
        self.log = logger.getLogger("Routes")
        self.directory_path = f"{os.environ['APP_PR_FILES']}"    
        self.prRoutes = PrRoutes(self, app)  
        self.debugURoutes = DebugUsersRoutes(self, app)   
        self.debugSRoutes = DebugServerRoutes(self, app)   
        self.debugDbRoutes = DebugDataBaseRoutes(self, app)   
        self.systemRoute = SystemRoutes(self, app)   

    
    def new_connection(self, connection):
        if not self.init:
            self.setup_routes()
            self.init = True
        self.conn = connection
        
    def setup_routes(self):        
        self.log.info("prepare all the routes")
        
        self.prRoutes.setup_routes()
        self.debugURoutes.setup_routes()          
        self.debugSRoutes.setup_routes()
        self.systemRoute.setup_routes()    
        self.debugDbRoutes.setup_routes()    
    
    def send(self, data, need_answer=False):
        self.log.info(f"Sending {data} with answer {need_answer}")
        self.answer = None
        jsonDump = json.dumps(data)
        dataB = bytes(jsonDump, encoding="utf-8")
        self.conn.send(dataB)  # send data to the client
        start_time = time.time()
        if need_answer:
            while (not self.answer) and ((time.time() - start_time) < 60):
                time.sleep(1)
                if self.answer:
                    return self.answer
            return {"error": "No answer received"}
        else:
            return None
        
        
    def received(self, answer):
        self.answer = answer
        self.log.info(f"Received: {answer}")
        
        


