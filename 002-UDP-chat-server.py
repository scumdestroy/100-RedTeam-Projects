import socket
import threading

# Set server address and port
server_address = ('localhost', 10000)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

# handle messages from clients
def handle_client_messages():
    while True:
        # Receive data from the client
        data, address = sock.recvfrom(4096)
        data = data.decode()
        print(f'Received {data} from {address}')


# Start a new thread to handle incoming messages
thread = threading.Thread(target=handle_client_messages)
thread.start()

# Run the server indefinitely
while True:
    # Send the message to the server
    message = input('Enter a message to send: ')
    sock.sendto(message.encode(), server_address)
