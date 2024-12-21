import socket, json, threading

class WebServer:
    def __init__(self, app, config):
        self.app = app
        self.setup_routes()
        self.setup_bot_server(config['cosmBot'])
        self.config = config
        
    def setup_bot_server(self, bot_config):
        # get the hostname
        host = bot_config['host']
        port = bot_config['port']  # initiate port no above 1024

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
        # look closely. The bind() function takes tuple as argument
        self.server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        conn = bot_config['maxConnect']
        conn=1 # at the moment only one is forced
        self.server_socket.listen(conn)
        thread = threading.Thread(target=self.run)
        self.stop_event = threading.Event()
        self.init = False
        thread.start()
        
    def run(self):
        print("ciapa")
        while True:            
            self.conn, self.address = self.server_socket.accept()  # accept new connection
            self.init = True
        
    def setup_routes(self):
        @self.app.get("/predict")            
        async def predict(x: float):
            k=1000
            if self.init:
                k=4
            y = x*k
            return {"result": y}                              