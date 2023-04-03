import socket
import select

# List of allowed IP addresses on the internal network
allowed_ips = ["192.168.1.100", "192.168.1.101"]

# Create a TCP/IP socket for the gateway
gateway_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the gateway socket to a specific address and port
gateway_address = ("", 8000)
gateway_sock.bind(gateway_address)

# Listen for incoming connections on the gateway socket
gateway_sock.listen(1)

# Create a list of sockets to monitor for incoming data
inputs = [gateway_sock]

while True:
    # Wait for incoming data on any of the monitored sockets
    readable, _, _ = select.select(inputs, [], [])

    for sock in readable:
        # If the incoming data is on the gateway socket, it's a new connection request
        if sock == gateway_sock:
            # Accept the incoming connection
            client_sock, client_address = sock.accept()
            print(f"New connection from {client_address}")

            # Check if the client IP address is allowed on the internal network
            if client_address[0] not in allowed_ips:
                print(f"Connection from {client_address} denied")
                client_sock.close()
                continue

            # If the client IP address is allowed, add the client socket to the list of monitored sockets
            inputs.append(client_sock)
        # If the incoming data is on a client socket, it's data from a connected client
        else:
            data = sock.recv(1024)
            if data:
                # Handle the incoming data here
                print(f"Received {len(data)} bytes from {sock.getpeername()}")
            else:
                # If the client socket has closed the connection, remove it from the list of monitored sockets
                print(f"Closing connection from {sock.getpeername()}")
                inputs.remove(sock)
                sock.close()
