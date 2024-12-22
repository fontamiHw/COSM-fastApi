import socket, time, threading
from fastapi_bridge.routes import Routes

class WebServer:
    def __init__(self, app, config, log):
        self.log = log
        self.app = app
        self.config = config
        self.setup_bot_server(config['socket'])
        self.routes = Routes(self.app, log)
        
    def setup_bot_server(self, bot_config):
        # get the hostname
        host = bot_config['host']
        port = bot_config['port']  # initiate port no above 1024

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
        while True:
            try:
                # look closely. The bind() function takes tuple as argument
                self.log.info(f"binding.... {host}:{port}")
                self.server_socket.bind((host, port))  # bind host address and port togeth
                self.log.info("binded")
                break #Exit
            except Exception as e:
                self.log.error(f"Exception {e}\n Wait ")
                time.sleep(bot_config['secErrorWait'])
        
        # configure how many client the server can listen simultaneously
        max_conn = bot_config['maxConnect']
        max_conn=1 # at the moment only one is forced
        self.log.info(f"listening max {max_conn} possible client connection ....")
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
                self.log.error(f"Exception {e}\n Wait nother connection.")
            
                                      