
from fastapi_bridge.model.item import Item

class PrItem(Item):
    type: str
    job:str | None = None
    status: str | None = None

    