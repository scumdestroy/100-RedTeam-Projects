import socket
import threading

# Set address and port
server_address = ('localhost', 10000)

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen()

def handle_client(conn, address):
    # Receive data from the client
    data = conn.recv(4096)
    data = data.decode()
    print(f'Received {data} from {address}')


def handle_incoming_connections():
    while True:
        conn, address = sock.accept()
        print(f'Accepted connection from {address}')

        # Start a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(conn, address))
        thread.start()

# Start a new thread to handle incoming connections
thread = threading.Thread(target=handle_incoming_connections)
thread.start()

# Run the server eternal
while True:
    message = input('Enter a message to send: ')
    for conn, address in connected_clients:
        conn.send(message.encode())
