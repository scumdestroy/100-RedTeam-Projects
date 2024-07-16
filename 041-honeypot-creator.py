import socket
import paramiko
from datetime import datetime

# Define the banner template
banner_template = """
Linux Console-MasterServer 6.1.0-22-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.94-1 (2024) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: {current_time} from {client_ip}
"""

class HoneyServer(paramiko.ServerInterface):
    def __init__(self, client_ip):
        self.client_ip = client_ip
        self.auth_attempts = 0
        self.log_file = open("honeypot_log.txt", "a")

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def get_banner(self):
        current_time = datetime.now().strftime('%a %b %d %H:%M:%S %Y')
        return banner_template.format(current_time=current_time, client_ip=self.client_ip), 'en'

    def check_auth_password(self, username, password):
        self.log_attempt(username, password)
        if self.auth_attempts == 0:
            self.auth_attempts += 1
            return paramiko.AUTH_PARTIALLY_SUCCESSFUL
        elif self.auth_attempts == 1:
            self.auth_attempts += 1
            return paramiko.AUTH_PARTIALLY_SUCCESSFUL
        elif self.auth_attempts == 2:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def log_attempt(self, username, password):
        self.log_file.write(f"IP: {self.client_ip}, Username: {username}, Password: {password}\n")
        self.log_file.flush()

    def close(self):
        self.log_file.close()

# Start the server and listen for connections
def start_ssh_server(host='0.0.0.0', port=22):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(100)

    while True:
        client_socket, client_addr = server_socket.accept()
        client_ip = client_addr[0]

        transport = paramiko.Transport(client_socket)
        transport.add_server_key(paramiko.RSAKey.generate(2048))
        ssh_server = HoneyServer(client_ip)

        try:
            transport.start_server(server=ssh_server)
            channel = transport.accept(20)
            if channel is None:
                continue

            channel.send("Root user login required to access console interface. All unauthorized access not permitted.\n")
            channel.send("Please enter root user's password: ")
            first_attempt = channel.recv(1024).decode().strip()
            ssh_server.log_attempt("root", first_attempt)
            channel.send("Password incorrect. Please try again.\n")
            channel.send("Please enter root user's password: ")
            second_attempt = channel.recv(1024).decode().strip()
            ssh_server.log_attempt("root", second_attempt)
            channel.send("One more attempt remaining before lockout. Please try again.\n")
            channel.send("Please enter root user's password: ")
            third_attempt = channel.recv(1024).decode().strip()
            ssh_server.log_attempt("root", third_attempt)
            channel.send("Root access granted.\n")

            banner = ssh_server.get_banner()[0]
            channel.send(banner)

            while transport.is_active():
                pass

        except paramiko.SSHException:
            pass

        transport.close()
        ssh_server.close()

if __name__ == '__main__':
    start_ssh_server()
