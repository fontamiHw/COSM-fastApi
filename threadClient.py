import socket
import json
import threading
import time

host = "192.168.1.75"
port = 5000  # Same port as the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
def start_client():

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        # Spawn a task (e.g., a long-running process)
        task_thread = threading.Thread(target=handle_task)
        task_thread.start()

        
        # Wait for the task to complete
        task_thread.join()

    finally:
        client_socket.close()



def handle_task():
    # Simulate some long-running task
    print("Task is running...")
    
    while True:
        # Receive the JSON data from the server
        data = client_socket.recv(1024)  # buffer size 1024 bytes
    
        # Deserialize JSON data
        print ('Retrieved',len(data),'characters')
        received_data = json.loads(data.decode("utf-8"))
        print(f"Received JSON data: {received_data}")

    print("Task completed.")

if __name__ == "__main__":
    print("start")
    start_client()
