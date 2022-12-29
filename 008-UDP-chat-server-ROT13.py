import socket
import string

def rot13(msg):
    # Create a translation table to use for the encoding
    trans_table = msg.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                    string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
                                    string.ascii_uppercase[13:] + string.ascii_uppercase[:13])

    # Use the translate method to encode the message
    enc_msg = message.translate(trans_table)

    return enc_msg

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 10001))

    print("CommServer initiated on port 10001. Prepare for incoming enemies.")

    while True:
        # get words
        data, addr = sock.recvfrom(1024)
        msg data.decode()
        print(f"Discovered a transmission from {addr}: {msg}")
        
        # send em back
        response = input("Speak now:)
        enc_response = rot13(response)
        sock.sendto(encoded_response.encode(), addr)

if __name__ == '__main__':
    main()
