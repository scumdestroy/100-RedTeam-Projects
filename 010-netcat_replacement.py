import sys
import socket
import time

# netcat at its core essence: drop it a host and port and make the connection.
host = sys.argv[1]
port = int(sys.argv[2])


# netcat function that prompts to send data and also awaits to receive something too
def nc(host_ip, pnum):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_ip, pnum))
    while True:
        msg = input()
        if msg == "":
            break
        s.sendall(msg.encode())
    time.sleep(3)

    while True:
        receiver = s.recv(1024)
        if not receiver:
            break
        print(receiver.decode())

    s.close()


# not quite as time-tested or feature-filled as netcat but its a start.
nc(host, port)
