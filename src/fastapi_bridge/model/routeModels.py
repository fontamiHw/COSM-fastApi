from pydantic import BaseModel

class Item(BaseModel):
    command: str | None = None
    

class PrItem(Item):
    type: str
    job:str | None = None
    status: str | None = None    