import socket
import struct
import textwrap

# create a raw socket and bind it to the network interface
conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
conn.bind(('wlan0', 0))

# process captured packets
while True:
    # capture a single packet
    raw_packet, addr = conn.recvfrom(65535)

    # parse the Ethernet header
    eth_header = raw_packet[:14]
    eth_fields = struct.unpack('!6s6sH', eth_header)
    eth_dest = eth_fields[0]
    eth_src = eth_fields[1]
    eth_type = socket.ntohs(eth_fields[2])

    # skip non-IP packets
    if eth_type != 0x0800:
        continue

    # parse the IP header
    ip_header = raw_packet[14:34]
    ip_fields = struct.unpack('!BBHHHBBH4s4s', ip_header)
    ip_ver = ip_fields[0] >> 4
    ip_ihl = ip_fields[0] & 0xF
    ip_tos = ip_fields[1]
    ip_len = ip_fields[2]
    ip_id = ip_fields[3]
    ip_off = ip_fields[4]
    ip_ttl = ip_fields[5]
    ip_proto = ip_fields[6]
    ip_sum = ip_fields[7]
    ip_src = socket.inet_ntoa(ip_fields[8])
    ip_dst = socket.inet_ntoa(ip_fields[9])

    # parse the TCP header
    tcp_header = raw_packet[34:54]
    tcp_fields = struct.unpack('!HHLLBBHHH', tcp_header)
    tcp_src = tcp_fields[0]
    tcp_dst = tcp_fields[1]
    tcp_seq = tcp_fields[2]
    tcp_ack = tcp_fields[3]
    tcp_off = tcp_fields[4] >> 4
    tcp_flags = tcp_fields[5]
    tcp_win = tcp_fields[6]
    tcp_sum = tcp_fields[7]
    tcp_urg = tcp_fields[8]

    # format and print the packet summary
    packet_summary = f'Packet from {ip_src}:{tcp_src} to {ip_dst}:{tcp_dst}\n'
    packet_summary += textwrap.indent(f'Flags: {tcp_flags:02X}\n', '    ')
    packet_summary += textwrap.indent(f'Seq: {tcp_seq}\n', '    ')
    packet_summary += textwrap.indent(f'Ack: {tcp_ack}\n', '    ')
    print(packet_summary)
