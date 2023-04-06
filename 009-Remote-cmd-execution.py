import socket
import sys

# Change these values to match your setup
host = 'friendlyvictimserver'
port = 8080

# init socket abilities
s = socket.socket()
s.connect((host, port))

# can also use `exec(cmd)` instead 
cmd = argv[1]
s.send(cmd.encode())

# get output
output = s.recv(1024).decode()
print(output)

s.close()
