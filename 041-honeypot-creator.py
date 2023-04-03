import socket

# Configure the honeypot server
honeypot_host = '0.0.0.0'
honeypot_port = 22
banner = "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3\r\n"

# Create the honeypot socket
honeypot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
honeypot_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
honeypot_socket.bind((honeypot_host, honeypot_port))
honeypot_socket.listen(1)

print("Honeypot server running on {}:{}".format(honeypot_host, honeypot_port))

# Accept incoming connections
while True:
    client_socket, address = honeypot_socket.accept()
    print("Connection from {}:{}".format(address[0], address[1]))

    # Send the banner
    client_socket.sendall(banner.encode())

    # Log any data received from the client
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data.decode().strip())

    client_socket.close()
