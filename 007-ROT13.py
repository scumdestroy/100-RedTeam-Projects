import string

def rot13(msg):
    # Whip up a gnarly trans_table for a clever ROT13 encoding
    trans_table = message.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                    string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
                                    string.ascii_uppercase[13:] + string.ascii_uppercase[:13])

    # translate method to encode 
    enc_msg = msg.translate(trans_table)

    return enc_msg

def main():
    msg = input("Enter a message to encode: ")
    enc_msg = rot13(msg)
    print(encoded_message)

if __name__ == '__main__':
    main()
