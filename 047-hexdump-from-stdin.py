import binascii

# binascii converts binary data to hex strings

def hexdump(data):
    # Split the data into chunks of 16 bytes and process each line as line of hex/ASCII data
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        hexy = ' '.join([f'{b:02X}' for b in chunk])
        texty = ''.join([chr(b) if 32 <= b < 127 else '.' for b in chunk])
        print(f'{i:04x} {hexy:<48} {texty}')

# input from stdin but a string won't work - it must be converted to bytes
data = bytes(input(), 'utf-8')

# big dump arrives
hexdump(data)
