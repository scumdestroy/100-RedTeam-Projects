import http.server
import socketserver
import ssl
import os
import datetime

# URL of the target webpage
url = "https://example.com"

# File name to save the downloaded webpage
filename = "target.html"

# Send a GET request to the target webpage and save the HTML content to a file
response = requests.get(url)
with open(filename, "w") as file:
    file.write(response.text)

# Set up the HTTPS server
port = 8000
certfile = "server.pem"
keyfile = "server.key"

handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", port), handler)

# Create a self-signed SSL certificate
os.system(f"openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out {certfile} -keyout {keyfile} -subj '/CN=localhost'")

# Wrap the server with SSL
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, keyfile=keyfile, server_side=True)

# Log incoming requests to a file
log_file = "server.log"
with open(log_file, "a") as file:
    file.write(f"[{datetime.datetime.now()}] Server started on port {port}\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    file.write(f"[{datetime.datetime.now()}] Server stopped\n")

