import socket, time, threading
from fastapi_bridge.routesBridge import RoutesBridge
import logger

class ContainerCommunication:
    def __init__(self, app, config):
        self.log = logger.getLogger("ContainerCommunication")
        self.config = config
        self.setup_bot_server(config['container_communication'])
        self.routes = RoutesBridge(app)
        
    def setup_bot_server(self, container_communication_config):
        # get the hostname
        host = container_communication_config['host']
        port = container_communication_config['port']  # initiate port no above 1024

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
                time.sleep(container_communication_config['secErrorWait'])
        
        # configure how many client the server can listen simultaneously
        max_conn = container_communication_config['maxConnect']
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
            
                                      