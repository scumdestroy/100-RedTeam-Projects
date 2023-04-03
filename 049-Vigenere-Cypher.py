def vigenere_cipher(text, key, mode):
    """
    Encrypts or decrypts the given text using the Vigenère Cipher with the given key.
    
    Parameters:
        text (str): The text to encrypt or decrypt.
        key (str): The key to use for the encryption or decryption.
        mode (str): The mode to use - 'encrypt' to encrypt the text, 'decrypt' to decrypt it.
    
    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""
    key_index = 0
    
    for i in range(len(text)):
        # If the current character is a letter, shift it by the corresponding key letter
        if text[i].isalpha():
            key_letter = key[key_index % len(key)]
            shift = ord(key_letter.upper()) - 65
            
            if mode == "encrypt":
                shifted_letter = chr((ord(text[i].upper()) + shift - 65) % 26 + 65)
            else:
                shifted_letter = chr((ord(text[i].upper()) - shift - 65) % 26 + 65)
            
            result += shifted_letter
            key_index += 1
        # Otherwise, leave it as is
        else:
            result += text[i]
    
    return result
