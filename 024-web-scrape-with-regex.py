import requests
import sys
import re

url = sys.argv[1]
response = requests.get(url)
content = response.text

# Enter a regex pattern of your choosing
# look for IP addresses: \b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b
# subdomains from page: (http[s]?:\/\/)?((-)?[\w+\.]){1,20}domain\.com
pattern = r'<PATTERN_HERE>' 
goal = re.findall(pattern, content)

print(goal)
