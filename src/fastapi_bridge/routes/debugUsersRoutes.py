import logger
from fastapi_bridge.routes.basicRouteClass import BasicRoute
from fastapi_bridge.model.routeModels import DebugItemUser
from fastapi import HTTPException


class DebugUsersRoutes(BasicRoute):
    
    def __init__(self, bridge, app):
        super().__init__(bridge, 'debug-users', app, logger.getLogger("DebugUsersRoutes"))
        
    def setup_routes(self):        
        self.log.info("   prepare all the DebugUsersRoutes routes")
        
        @self.app.get('/debug/users')
        async def get_user(admin: bool=False):
            item = DebugItemUser()   
            item.only_admin = admin           
            item_dict = self.add_command(item)
            self.log.info(f"received from path /debug : {item_dict}")
            answer = self.send(item_dict, need_answer=True)
            return answer     
       
