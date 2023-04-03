import argparse
import concurrent.futures
import socket

## Run via cmd line like: python3 subdomain_enumerator.py example.com wordlist.txt



# List of popular DNS resolvers
resolvers = ["1.1.1.1", "8.8.8.8"]

def resolve(domain, subdomain, resolver):
    """Resolve a subdomain using a DNS resolver."""
    try:
        ip_address = socket.gethostbyname(f"{subdomain}.{domain}", resolver)
        print(f"[{resolver}] {subdomain}.{domain}: {ip_address}")
    except socket.gaierror:
        pass

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Enumerate subdomains.")
    parser.add_argument("domain", help="The domain name to enumerate subdomains for.")
    parser.add_argument("wordlist", help="The wordlist file containing subdomains to test.")
    args = parser.parse_args()

    # Load the wordlist file
    with open(args.wordlist) as f:
        subdomains = [line.strip() for line in f]

    # Use multiple threads to test the subdomains against each resolver
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit each subdomain and resolver combination as a separate task to the executor
        tasks = []
        for subdomain in subdomains:
            for resolver in resolvers:
                tasks.append(executor.submit(resolve, args.domain, subdomain, resolver))

        # Wait for all tasks to complete
        concurrent.futures.wait(tasks)
