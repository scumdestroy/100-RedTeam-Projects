from Crypto.PublicKey import RSA
import base64

# Generate a new RSA key pair
key = RSA.generate(2048)

# Get the public key in PEM format
public_key = key.publickey().export_key()

# Encode the public key using base64
encoded_public_key = base64.b64encode(public_key).decode('utf-8')

# Print the encoded public key
print("Public key:\n{}".format(encoded_public_key))

# Get the private key in PEM format
private_key = key.export_key()

# Encode the private key using base64
encoded_private_key = base64.b64encode(private_key).decode('utf-8')

# Print the encoded private key
print("Private key:\n{}".format(encoded_private_key))
