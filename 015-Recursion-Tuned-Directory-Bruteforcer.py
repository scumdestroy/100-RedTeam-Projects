import argparse
import requests
import threading
import time
import sys
from bs4 import BeautifulSoup

def main(domain, wordlist, jitter, threads, recursive):
    urls = []
    with open(wordlist, 'r') as f:
        for line in f:
            url = domain + line.strip()
            urls.append(url)

    thread_list = []
    for i in range(threads):
        t = threading.Thread(target=check_urls, args=(urls, jitter, recursive))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

def check_urls(urls, jitter, recursive):
    # Check each URL in the list
    for url in urls:
        try:
            # Make a request to the URL
            response = requests.get(url)

            # Print the details of the response
            print(f"URL: {response.url}")
            print(f"Title: {get_title(response)}")
            print(f"Length: {len(response.content)}")
            print(f"Status Code: {response.status_code}")

            # If recursion is enabled, check all links on the page
            if recursive:
                soup = BeautifulSoup(response.content, 'html.parser')
                links = soup.find_all('a')
                for link in links:
                    new_url = link.get('href')
                    if new_url.startswith('/'):
                        new_url = url + new_url
                    elif not new_url.startswith('http'):
                        new_url = url + '/' + new_url
                    check_urls([new_url], jitter, False)

            # Sleep for a random amount of time to avoid being detected as a bot
            time.sleep(jitter)

        except Exception as e:
            print(f"Error checking URL {url}: {e}")

def get_title(response):
    # Extract the title from the response
    soup = BeautifulSoup(response.content, 'html.parser')
    title_tag = soup.find('title')
    if title_tag is not None:
        return title_tag.string.strip()
    else:
        return ''

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Check URLs on a domain.')
    parser.add_argument('domain', help='The domain to check URLs on.')
    parser.add_argument('wordlist', help='The path to the wordlist to use.')
    parser.add_argument('--jitter', type=float, default=1.0,
                        help='The maximum amount of jitter to use between requests (in seconds).')
    parser.add_argument('--threads', type=int, default=10,
                        help='The number of concurrent threads to use.')
    parser.add_argument('--recursive', action='store_true',
                        help='Enable recursive checking of links on the pages.')
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args.domain, args.wordlist, args.jitter, args.threads, args.recursive)
