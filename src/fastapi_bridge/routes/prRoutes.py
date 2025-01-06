import logger
from fastapi_bridge.model.routeModels import PrItem
from fastapi import File, HTTPException, UploadFile
from fastapi_bridge.routes.basicRouteClass import BasicRoute


class PrRoutes(BasicRoute):
    def __init__(self, bridge, app):
        super().__init__(bridge, app, logger.getLogger("Routes"))
    
    def setup_routes(self):        
        self.log.info("   prepare all the  Pr routes")
        
        @self.app.post('/pr')
        async def post_pr(item: PrItem):            
            item_dict= self.add_command(item, 'pr')
            self.log.info(f"received from path /pr : {item_dict}")
            self.bridge.send(item_dict)
            return {"message": "command processed"}

        @self.app.post('/pr/file')
        def upload_pr_file(file: UploadFile = File(...)):
            item_dict = {'command': 'prFile', 'filename': file.filename}        
            self.log.info(f"received from path /pr/file : {item_dict}")
            sent = False
            try:
                contents = file.file.read()
                with open(f"{self.directory_path}/{file.filename}", 'wb') as f:
                    f.write(contents)                
                sent = True
            except Exception:
                raise HTTPException(status_code=500, detail='Something went wrong')
            finally:
                file.file.close()
                if sent:
                    self.bridge.send(item_dict)

            return {"message": f"Successfully uploaded {file.filename}"}      