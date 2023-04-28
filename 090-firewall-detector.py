from scapy.all import *

# Define a destination IP address and port to test
dst_ip = '192.168.0.1'
dst_port = 80

# Create a TCP SYN packet to send to the destination
syn_packet = IP(dst=dst_ip) / TCP(dport=dst_port, flags='S')

# Send the SYN packet and wait for a response
response = sr1(syn_packet, timeout=2, verbose=False)

# Check if a response was received
if response is not None:
    # Check if the response contains a TCP SYN-ACK flag
    if response.haslayer(TCP) and response[TCP].flags == 0x12:
        # A SYN-ACK was received, indicating that the port is open
        print("Port {} is open, firewall is likely not present".format(dst_port))
    else:
        # A response was received, but the port is not open or the response is not a SYN-ACK
        print("Port {} is not open, firewall may be present".format(dst_port))
else:
    # No response was received, indicating that the port may be filtered by a firewall
    print("No response received, firewall may be present")
