import socket
import struct
import platform

# The IP address range to scan
ip_dest = argv[1]

# The port range to scan
PORT_RANGE = range(1, 1024)

# The TTL values for common operating systems
OS_TTL = {
    "Windows": 128,
    "Linux, BSD, Solaris or Mac": 64,
}

# Get the current operating system
current_os = platform.system()

# Create a raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Set the socket timeout
s.settimeout(1)

# Iterate through each port in the range
for port in PORT_RANGE:
    # Set the destination port
    dest_addr = (ip_dest, port)

    # Send a packet to the destination
    s.sendto(b"", dest_addr)

    # Try to receive a packet from the destination
    try:
        data, addr = s.recvfrom(1024)
        ttl = struct.unpack("!B", data[8:9])[0]

        # Check the TTL value against the known values for each operating system
        os_guess = None
        for os_name, os_ttl in OS_TTL.items():
            if ttl == os_ttl:
                os_guess = os_name
                break

        # Print the results
        print(f"{addr[0]}:{addr[1]} is open (TTL: {ttl}, guessed OS: {os_guess})")
    except socket.timeout:
        # If no response is received, the port is closed
        pass

# Close the socket
s.close()
