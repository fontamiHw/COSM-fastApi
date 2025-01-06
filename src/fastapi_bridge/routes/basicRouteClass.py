class BasicRoute(object):
    def __init__(self, bridge, app, log):
        self.app = app  
        self.log = log
        self.bridge = bridge
        
            
    def add_command(self, item, command):
        item.command = command
        return item.model_dump()

