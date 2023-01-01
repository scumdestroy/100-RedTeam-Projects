import socket
import struct

# The IP address range to scan
ip_dest = argv[1]

# Commonly used ports + a few of my favorite vulnerable bug bounty/interesting shodan-able ones thrown in
common_ports = [80, 137, 433, 123, 138, 1434, 445, 136, 67, 23, 21, 139, 22, 68, 8080, 8433, 8080, 25, 111, 110, 998, 53, 2222, 135, 3306, 2049, 1433, 3456, 443, 7, 5900]

# Alternate: use range of ports
# PORT_RANGE = range(1, 1024)
# Iterate through each port in the range
# for port in PORT_RANGE:
for port in common_ports:
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
        print(f"{addr[0]}:{addr[1]} is open (TTL: {ttl}, likely OS: {os_guess})")
    except socket.timeout:
        # If no response is received, the port is closed
        pass

# Close the socket
s.close()
