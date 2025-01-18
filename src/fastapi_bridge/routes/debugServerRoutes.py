import logger
from fastapi_bridge.routes.basicRouteClass import BasicRoute
from fastapi_bridge.model.routeModels import  DebugItemServer
from fastapi import HTTPException
from fastapi import FastAPI

class DebugServerRoutes(BasicRoute):
    
    def __init__(self, bridge, app: FastAPI):
        super().__init__(bridge, 'debug-server', app, logger.getLogger("DebugServerRoutes"))
        
    def setup_routes(self):        
        self.log.info("   prepare all the  DebugServerRoutes routes")        
        
        @self.app.get('/debug/server')
        async def get_server_data(server: str='Git', admin: str=None):
            if not admin:
                raise HTTPException(status_code=500, detail='admin username is mandatory')
            item = DebugItemServer()
            item.server = server
            item.admin = admin
            item_dict = self.add_command(item)
            self.log.info(f"received from path /debug : {item_dict}")
            self.send(item_dict)
            return {"message": "result on the log of the received application"}
