import logger
from fastapi_bridge.routes.basicRouteClass import BasicRoute
from fastapi_bridge.model.routeModels import DebugItemUser, DebugItemServer


class DebugRoutes(BasicRoute):
    
    def __init__(self, bridge, app):
        super().__init__(bridge, app, logger.getLogger("DebugRoutes"))
        
    def setup_routes(self):        
        self.log.info("   prepare all the  Debug routes")
        
        @self.app.get('/debug/users')
        async def get_user(admin: bool=False):
            item = DebugItemUser()   
            item.only_admin = admin           
            item_dict= self.add_command(item, 'debug-users')
            self.log.info(f"received from path /debug : {item_dict}")
            self.bridge.send(item_dict)
            return {"message": "result on the log of the received application"}
        
        @self.app.get('/debug/server')
        async def get_server_data(server: str='Git'):
            item = DebugItemServer()
            item.server = server
            item_dict= self.add_command(item, 'debug-server')
            self.log.info(f"received from path /debug : {item_dict}")
            self.bridge.send(item_dict)
            return {"message": "result on the log of the received application"}
