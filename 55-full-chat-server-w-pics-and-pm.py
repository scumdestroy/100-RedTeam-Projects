import socket
import threading
import os
import sys

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8888)
server.bind(server_address)
server.listen(5)
print('Server is listening on', server_address)

# Set up the clients list and messages dictionary
clients = []
messages = {}

# Define the message handler function
def handle_message(client_socket, client_address):
    # Receive the client's username
    client_name = client_socket.recv(1024).decode('utf-8')
    clients.append(client_socket)
    print('New client connected:', client_name)

    # Send a welcome message to the client
    welcome_message = 'Welcome to the chat room, ' + client_name + '!\n'
    client_socket.sendall(welcome_message.encode('utf-8'))

    while True:
        try:
            # Receive the message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if message.startswith('/pm'):
                # Parse the private message
                message_parts = message.split(' ')
                recipient = message_parts[1]
                message_text = ' '.join(message_parts[2:])

                # Find the recipient client
                recipient_socket = None
                for c in clients:
                    if c != client_socket and c.getpeername()[1] == client_socket.getpeername()[1]:
                        recipient_socket = c
                        break

                # Send the private message to the recipient
                if recipient_socket is not None:
                    pm_message = client_name + ' (private): ' + message_text + '\n'
                    recipient_socket.sendall(pm_message.encode('utf-8'))
                    client_socket.sendall(pm_message.encode('utf-8'))
                else:
                    error_message = 'Recipient not found.\n'
                    client_socket.sendall(error_message.encode('utf-8'))
            elif message.startswith('/file'):
                # Parse the file name and size
                message_parts = message.split(' ')
                file_name = message_parts[1]
                file_size = int(message_parts[2])

                # Receive the file from the client
                received_size = 0
                file_data = b''
                while received_size < file_size:
                    data = client_socket.recv(1024)
                    received_size += len(data)
                    file_data += data

                # Save the file to disk
                with open(file_name, 'wb') as f:
                    f.write(file_data)

                # Send the file to all clients
                file_message = client_name + ' sent a file: ' + file_name + '\n'
                for c in clients:
                    if c != client_socket:
                        c.sendall(file_message.encode('utf-8'))
            elif message.startswith('/image'):
                # Parse the image name and size
                message_parts = message.split(' ')
                image_name = message_parts[1]
                image_size = int(message_parts[2])

                # Receive the image from the client
                received_size = 0
                image_data = b''
                while received_size < image_size:
                    data = client_socket.recv(1024)
                    received_size += len(data)
                    image_data += data

                # Save the image to disk
                with open(image_name, 'wb') as f:
                    f.write(image_data)

                # Send the image to all clients
                image_message = client_name + ' sent an image: ' + image_name + '\n'
            for c in clients:
                if c != client_socket:
                    c.sendall(image_message.encode('utf-8'))
        else:
            # Broadcast the message to all clients
            broadcast_message = client_name + ': ' + message + '\n'
            for c in clients:
                if c != client_socket:
                    c.sendall(broadcast_message.encode('utf-8'))

            # Save the message to the history
            if client_name not in messages:
                messages[client_name] = []
            messages[client_name].append(broadcast_message)

    except ConnectionResetError:
        # Handle the case when the client disconnects
        clients.remove(client_socket)
        print('Client disconnected:', client_name)
        break
