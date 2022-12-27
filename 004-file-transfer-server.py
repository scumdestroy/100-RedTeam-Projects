import socketserver

class FileTransferHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Receive the file from the client
        file_data = self.request.recv(4096)

        # Save the file to the server's file system
        with open('received_file.txt', 'wb') as f:
            f.write(file_data)

# Create the server
server = socketserver.TCPServer(('localhost', 8008), FileTransferHandler)

# Run the server indefinitely
server.serve_forever()
