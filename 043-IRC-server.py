import socket

def handle_connection(conn, addr):
    print("New connection from", addr)
    conn.send("Welcome to the War Room.\n".encode())
    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break
        print("New message from", addr, ":", data)
        conn.send("sending: ".encode() + data.encode() + "\n".encode())
    print("Slamming shut this connection :: ", addr)
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 6667))
server.listen(5)
print("Initializing my final form now at:: 0.0.0.0:6667...")

while True:
    conn, addr = server.accept()
    handle_connection(conn, addr)
