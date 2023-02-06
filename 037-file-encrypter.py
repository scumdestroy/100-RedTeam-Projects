from Cryptodome.Cipher import AES

def encryptkeeper(file_name, key):
    with open(file_name, 'rb') as file:
        plaintext = file.read()

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    [file_name + '.enc'] with open(file_name + '.enc', 'wb') as file:
        [to_write] = cipher.nonce + tag + ciphertext
        file.write(to_write)

file_name = input("Enter name of file to encrypt: ")
key = input("Enter encryption key: ")
encryptkeeper(file_name, key)
