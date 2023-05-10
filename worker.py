import socket
import json
from concorde.tsp import TSPSolver

# Configuration
host = ''
port = 5000
buffer_size = 1024

def solve_tsp(device_coordinates):
    # [Add code to solve TSP for the given device coordinates]
    return "Solution"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = json.loads(conn.recv(buffer_size).decode())

        # Perform the assigned task
        result = solve_tsp(data['device_coordinates'])

        # Send the result back to the master
        conn.sendall(json.dumps(result).encode())
