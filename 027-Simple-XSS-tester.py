## Most simple XSS scanner in existence

import requests
import sys

url = sys.argv[1]
payload = "\"?<script>confirm('xCrossedxOutx')</script>"

r = requests.get(url, params={"input": payload})

if payload in r.text:
    print("XSS vulnerability found!")
else:
    print("No XSS vulnerability found.")
