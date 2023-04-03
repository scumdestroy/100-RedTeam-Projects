from scapy.all import *

# set the wireless interface to capture packets from
iface = "wlan0"

# set the BSSID (MAC address of the access point) to filter on
bssid = "00:11:22:33:44:55"

# set the ESSID (network name) to filter on
essid = "MyWiFiNetwork"

# set the number of packets to capture
num_packets = 1000

# create a function to handle captured packets
def packet_handler(pkt):
    global handshake
    # check if the packet is a wireless management frame
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:  # management frame, beacon
            # check if the packet matches the BSSID and ESSID filters
            if pkt.addr3 == bssid and pkt.info == essid:
                # check if the packet is part of a handshake
                if pkt.haslayer(Dot11Elt) and pkt[Dot11Elt].ID == 48:
                    if not handshake:
                        handshake = [pkt]
                    else:
                        handshake.append(pkt)
                    if len(handshake) == 4:
                        print("Valid handshake captured!")
                        print("".join([pkt[Dot11Elt].info.decode() for pkt in handshake]))
                        # you can save the handshake to a file or process it further
                        # reset the handshake list
                        handshake = []

# start capturing packets on the wireless interface
handshake = []
sniff(iface=iface, prn=packet_handler, count=num_packets)
