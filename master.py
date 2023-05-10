import socket
import json

# Configuration
worker_ips = ['192.168.1.2', '192.168.1.3', '192.168.1.4']
worker_port = 5000
buffer_size = 1024

# Divide the TSP problem into smaller tasks and send them to the workers
for i, worker_ip in enumerate(worker_ips):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((worker_ip, worker_port))

        task = {
            'task_id': i,
            'device_coordinates': [
                (1, 1),
                (4, 3),
                (6, 2),
                (8, 4)
            ]
        }
        s.sendall(json.dumps(task).encode())

        # Receive results from the worker
        result = json.loads(s.recv(buffer_size).decode())
        print(f"Result from worker {i}: {result}")
