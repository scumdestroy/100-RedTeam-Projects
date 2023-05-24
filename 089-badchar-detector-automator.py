import subprocess

target_application = "path/to/application"
vulnerable_buffer = "A" * 1000  # Adjust the buffer size as needed

all_characters = bytearray(range(256))
bad_characters = bytearray(b"\x00\x0A\x0D")  

# Remove bad boys from payload 
payload = bytearray()
for char in all_characters:
    if char not in bad_characters:
        payload.append(char)

# Lenghty but very chill way to automate bad character detection.  So just pour yourself a lemonade and take a nap while we weed these bad boys out
try:
    subprocess.run([target_application, payload], input=vulnerable_buffer, check=True)
except subprocess.CalledProcessError:
    # Crash occurs - identify bad boys
    detected_bad_characters = bytearray()
    for char in payload:
        test_payload = vulnerable_buffer + bytes([char])
        try:
            subprocess.run([target_application, test_payload], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            detected_bad_characters.append(char)

    print("Detected bad characters:", detected_bad_characters)
