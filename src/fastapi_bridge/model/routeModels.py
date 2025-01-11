from pydantic import BaseModel

class Item(BaseModel):
    command: str | None = None
    

class PrItem(Item):
    type: str
    job:str | None = None
    status: str | None = None    
    

class DebugItemSystem(Item):
    status: bool | None = True
    

class DebugItemUser(Item):
    only_admin: bool | None = False
    

class DebugItemServer(Item):
    server: str | None = 'Git'
    admin: str | None = None
    