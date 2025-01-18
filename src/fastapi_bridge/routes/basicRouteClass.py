

class BasicRoute(object):
    def __init__(self, bridge, command: str, app, log):
        self.app = app  
        self.log = log
        self.bridge = bridge
        self.command = command
        
            
    def add_command(self, item):
        item.command = self.command
        return item.model_dump()
    
    def send(self, data, need_answer=False):
        return self.bridge.send(data, need_answer)

