import logger
from fastapi_bridge.routes.basicRouteClass import BasicRoute
from fastapi_bridge.model.routeModels import DebugItemSystem
from fastapi import HTTPException


class SystemRoutes(BasicRoute):
    
    def __init__(self, bridge, app):
        super().__init__(bridge, 'system', app, logger.getLogger("SystemRoutes"))
        
    def setup_routes(self):        
        self.log.info("   prepare all the SystemRoutes routes")
        
        @self.app.get('/system')
        async def get_user(status: bool=True):
            item = DebugItemSystem()   
            item.status = status           
            item_dict = self.add_command(item)
            self.log.info(f"received from path /system : {item_dict}")
            self.send(item_dict)
            return {"message": "result on the log of the received application"}
