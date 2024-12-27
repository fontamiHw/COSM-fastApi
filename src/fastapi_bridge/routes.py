import socket, json, threading
import logger

class Routes:
    def __init__(self, app):
        self.app = app  
        self.init = False
        self.log = logger.getLogger("Routes")
    
    def new_connection(self, connection):
        if not self.init:
            self.setup_routes()
            self.init = True
        self.conn = connection
        
    def setup_routes(self):
        self.log.info("prepare all the routse")
        
        @self.app.get("/predict")            
        async def predict(x: float):
            self.log.info(f" Invoked /predict with x={x}")
            k=1000
            if self.conn:
                k=4
                y = x*k
                data =  {"result": y}
                self.send(data)
                return data     
    
    def send(self, data):
        self.log.info(f"Sending {data}")
        jsonDump = json.dumps(data)
        dataB = bytes(jsonDump, encoding="utf-8")
        self.conn.send(dataB)  # send data to the client
        
        # @self.app.post('/pr')
        # def receive_json():
        #     data = request.get_json()
        #     if not data:
        #         return jsonify({"error": "No JSON data provided"}), 400
            
        #     # Process the JSON data here
        #     data = self.jenkins.event_received(data)
        #     return jsonify({"message": "JSON data received", "data": data}), 200

        # @self.app.route('/pr/file', methods=['POST'])
        # def receive_file():
        #     if 'file' not in request.files:
        #         return jsonify({"error": "No file part in the request"}), 400
        #     file = request.files['file']
        #     if file.filename == '':
        #         return jsonify({"error": "No selected file"}), 400
        #     # Save the file or process it here
        #     file.save(f"./{file.filename}")
        #     return jsonify({"message": "File received", "filename": file.filename}), 200
