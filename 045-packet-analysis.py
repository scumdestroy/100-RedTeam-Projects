import scapy.all as scapy

def sniffem(interface):
    scapy.sniff(iface=interface, prn=analyze_em)

def analyze_em(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        payload = ""
        if packet.haslayer("TCP"):
            payload = packet["TCP"].payload
        elif packet.haslayer("UDP"):
            payload = packet["UDP"].payload
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Payload: {payload}")
        
        # function that saves packets to .pcap file for further wireshark analysis, append=True so it doesn't overwrite 
        scapy.wrpcap("captured_packets.pcap", packet, append=True)

sniffem("wlan0")
