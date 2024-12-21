
class WebServer:
    def __init__(self, app):
        self.app = app
        self.setup_routes()
        

    def setup_routes(self):
        @self.app.get("/predict")
        async def predict(x: float):
            y = x*4
            return {"result": y}                              