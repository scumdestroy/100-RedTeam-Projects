import socket
import time

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
msg_server = ('localhost', 8000)
print('Summoning a server at {} and port {}'.format(*msg_server))
s.bind(msg_server)

# Listen for incoming connections
s.listen(1)

while True:
    # Server is up successfully...
    print('Ready for action...')
    connection, client_addr = s.accept()
    try:
        print('Received a connection from: ', client_addr)

        # Receive the data in small chunks and echo back to client
        while True:
            data = connection.recv(16)
            print('Something has arrived... {!r}'.format(data))
            if data:
                print('Reflecting data to client to signify message success.')
                connection.sendall(data)
                last_msg = time.time()
            else:
                # if nothing received for 20 seconds, kill the connection
                print('dead air from: ', client_address)
                if time.time() - last_msg > 20:
                    print('shut it down')
                    s.close()
                    break
                break
            
    finally:
        # Clean up the connection
        connection.close()
