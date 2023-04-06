import argparse
import requests
import threading

def main(url, wordlist, threads):
    dirs = []
    with open(wordlist, 'r') as f:
        for line in f:
            dirs.append(line.strip())
    thread_list = []
    for i in range(threads):
        t = threading.Thread(target=check_dirs, args=(url, dirs))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

def check_dirs(url, dirs):
    for dir in dirs:
        try:
            response = requests.get(url + dir)

            # If the directory exists, print it
            if response.status_code == 200:
                print(f"Directory found: {url + dir}")

        except Exception as e:
            print(f"Error checking directory {url + dir}: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Brute-force directories on a website.')
    parser.add_argument('url', help='The URL of the website to check.')
    parser.add_argument('wordlist', help='The path to the wordlist to use.')
    parser.add_argument('--threads', type=int, default=10,
                        help='The number of concurrent threads to use.')
    args = parser.parse_args()

    main(args.url, args.wordlist, args.threads)
