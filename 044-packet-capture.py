from scapy.all import *

def print_pkt(pkt):
    if IP in pkt:
        print("Source: {0}, Destination: {1}".format(pkt[IP].src, pkt[IP].dst))

sniff(prn=print_pkt)
