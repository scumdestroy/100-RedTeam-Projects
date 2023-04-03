import requests

# Define target URL
url = 'http://example.com'

# Make a request to the target website
response = requests.get(url)

# Extract information from response headers
server_header = response.headers.get('Server', None)
x_powered_by_header = response.headers.get('X-Powered-By', None)
x_xss_protection_header = response.headers.get('X-XSS-Protection', None)

# Print extracted information
print(f'Server header: {server_header}')
print(f'X-Powered-By header: {x_powered_by_header}')
print(f'X-XSS-Protection header: {x_xss_protection_header}')
