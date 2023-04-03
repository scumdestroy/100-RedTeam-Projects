import socket

# List of allowed IP addresses
allowed_ips = ["192.168.1.100", "192.168.1.101"]

# List of allowed ports
allowed_ports = [80, 22, 443]

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ("", 8000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()

    # Check if the client IP address is allowed
    if client_address[0] not in allowed_ips:
        print(f"Connection from {client_address[0]} denied")
        connection.close()
        continue

    # Check if the client is trying to connect to an allowed port
    if client_address[1] not in allowed_ports:
        print(f"Connection from {client_address[0]} to port {client_address[1]} denied")
        connection.close()
        continue

    # If the connection is allowed, handle it
    print(f"Connection from {client_address[0]} to port {client_address[1]} allowed")
    # Handle the connection here
