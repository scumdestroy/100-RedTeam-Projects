import sys
import requests

## note: I wasn't 100% sure what a googlebot scan was, so my best assumption is to compare a page w/ different user-agents, one being "Googlebot" to see if any bypasses are present

url = sys.argv[1]

# Make request with Googlebot user-agent
headers = {'User-Agent': 'Googlebot'}
googlebot_response = requests.get(url, headers=headers)
googlebot_html = googlebot_response.text

# Make request with Chrome user-agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
chrome_response = requests.get(url, headers=headers)
chrome_html = chrome_response.text

# Compare HTML content and highlight differences
if chrome_html != googlebot_html:
    print("Differences found:")
    for line in difflib.unified_diff(chrome_html.splitlines(), googlebot_html.splitlines()):
        print(line)
else:
    print("No differences found.")
