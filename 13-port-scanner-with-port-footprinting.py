# after an onslaught of socket module scripts, I give myself permission to take it easy for this one

import nmap

def scan_ports(host, start_port, end_port):
    # Init nmap.PortScanner class
    scanner = nmap.PortScanner()

    # Scan em and slam em for the long game
    results = scanner.scan(host, f"{start_port}-{end_port}")

    # Get the list of open ports from the scan results
    open_ports = [p for p in results['scan'] if results['scan'][p]['tcp']['state'] == 'open']
    return open_ports

def main():
    host = input("Enter host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the final port: "))


    open_ports = scan_ports(host, start_port, end_port)
    print(f"Open ports: {open_ports}")

if __name__ == '__main__':
    main()
