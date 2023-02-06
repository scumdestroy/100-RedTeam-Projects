import smtplib
from email.mime.text import MIMEText

def send_email(to_list, subject, message):
    sender = "spamdaddy@babyhouse.com"
    password = "666baby666"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(to_list)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, to_list, msg.as_string())

def read_emails_from_file(file_path):
    with open(file_path, "r") as file:
        return [email.strip() for email in file.readlines()]

email_file = "emails.txt"
subject = "Not SPAM"
message = "Just some non-malicious links for you to browse, my friend."

email_list = read_emails_from_file(email_file)
send_email(email_list, subject, message)
