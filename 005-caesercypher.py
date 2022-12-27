def caesar_cipher(plaintext: str) -> str:
    # Create a mapping of the alphabet to the shifted alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[3:] + alphabet[:3]
    mapping = str.maketrans(alphabet, shifted_alphabet)

    # Use the mapping to encode the plaintext
    ciphertext = plaintext.translate(mapping)
    return ciphertext
  
  caesar_cipher(argv[1])
