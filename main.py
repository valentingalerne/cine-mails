import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bo.send_mail import *

ADDRESS = "super.6nez@gmail.com"
PASSWORD = "P@ssw0rD"

names, emails = get_contacts('./files/address.txt')
message_template = read_template('./files/template.txt')


s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(ADDRESS, PASSWORD)

for name, email in zip(names, emails):
    msg = MIMEMultipart()

    message = message_template.substitute(USERNAME=name.title())

    print(message)

    msg['From'] = ADDRESS
    msg['To'] = email
    msg['Subject'] = "This is TEST"

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)
    del msg

s.quit()


print('Hello world')
