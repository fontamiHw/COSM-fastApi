import socket, time, threading
from fastapi_bridge.routes import Routes

class WebServer:
    def __init__(self, app, config):
        self.app = app
        self.setup_bot_server(config['cosmBot'])
        self.config = config
        self.routes = Routes(self.app)
        
    def setup_bot_server(self, bot_config):
        time.sleep(5)
        # get the hostname
        host = bot_config['host']
        port = bot_config['port']  # initiate port no above 1024

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
        while True:
            try:
                # look closely. The bind() function takes tuple as argument
                print(f"connecting.... {host}:{port}")
                self.server_socket.bind((host, port))  # bind host address and port togeth
                print(f"connected")
                break #Exit
            except Exception as e:
                print(f"ecezione {e}")
                time.sleep(60)
        print(f"connected2")
        # configure how many client the server can listen simultaneously
        max_conn = bot_config['maxConnect']
        max_conn=1 # at the moment only one is forced
        self.server_socket.listen(max_conn)
        thread = threading.Thread(target=self.run)
        self.stop_event = threading.Event()        
        thread.start()
        
    def close_all(self):
        self.conn.close()
    
    def run(self):
        while True:  
            try:          
                self.conn, self.address = self.server_socket.accept()  # accept new connection
                self.routes.new_connection(self.conn)
            except Exception as e:
                print("ecezione")
                print(f"{e}")
            
                                      