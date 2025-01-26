import logger
from fastapi_bridge.routes.basicRouteClass import BasicRoute
from fastapi_bridge.model.routeModels import  DebugItemDb
from fastapi import HTTPException
from fastapi import FastAPI

class DebugDataBaseRoutes(BasicRoute):
    
    def __init__(self, bridge, app: FastAPI):
        super().__init__(bridge, 'db', app, logger.getLogger("debugDataBaseRoutes"))
        
    def setup_routes(self):        
        self.log.info("   prepare all the  debugDataBaseRoutes routes")        
        
        @self.app.get('/debug/db')
        async def get_db_data(db: str='users', admin: str=None):
            if not admin:
                raise HTTPException(status_code=500, detail='admin username is mandatory')
            item = DebugItemDb()
            item.db = db
            item.admin = admin
            item_dict = self.add_command(item)
            self.log.info(f"received from path /debug : {item_dict}")
            answer = self.send(item_dict, need_answer=True)
            return answer
