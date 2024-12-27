import socket
import json
import threading
import time

host = "127.0.0.1"
port = 5000  # Same port as the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
def start_client():
    """
    Starts the client, connects to the server, and spawns a task in a separate thread.
    This function performs the following steps:
    1. Connects to the server using the specified host and port.
    2. Prints a message indicating a successful connection.
    3. Spawns a new thread to handle a long-running task.
    4. Waits for the task to complete.
    5. Closes the client socket connection.
    Note:
        The variables `client_socket`, `host`, `port`, and the function `handle_task`
        should be defined elsewhere in the code.
    Raises:
        Any exceptions raised during the connection or task execution will be propagated.
    """
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
