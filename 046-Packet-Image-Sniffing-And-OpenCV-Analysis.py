import cv2
import numpy as np
import pytesseract
import scapy.all as scapy

# Note: also requires Tesseract OCR engine (through apt or yum or something)


def sniff_packets(interface):
    scapy.sniff(iface=interface, prn=process_packet)

def process_packet(packet):
    if packet.haslayer("Raw"):
        raw_data = packet["Raw"].load
        np_data = np.frombuffer(raw_data, dtype=np.uint8)
        img = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
        if img is not None:
            # Detect text and faces in the image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # pytesseract will detect text via converting to greyscale and using 'image_to_string' function to search for anything valid
            text = pytesseract.image_to_string(gray)
            # the `cv2.CascadeClassifier` class and the `detectMultiScale` method are used to detect human faces 
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(text) > 0:
                print("Image contains text")
            elif len(faces) > 0:
                print("Image contains a human face")
            else:
                print("Image does not contain text or a human face")

sniff_packets("wlan0")
