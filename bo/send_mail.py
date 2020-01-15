from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
import configparser

def read_template(filename):
    with open(filename, mode='r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def get_contacts(filename):
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact)
    return emails


def send(error, errorName):
    config = configparser.ConfigParser()
    config.read('./address.ini')

    ADDRESS = config['data_address']['address']
    PASSWORD = config['data_address']['password']

    emails = get_contacts('./files/address.txt')
    message_template = read_template('./files/template.txt')

    smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtp.starttls()
    smtp.login(ADDRESS, PASSWORD)

    for email in emails:
        msg = MIMEMultipart()

        message = message_template.substitute(NUM_ERROR=str(error))
        print(message)

        msg['From'] = ADDRESS
        msg['To'] = email
        msg['Subject'] = "[Erreur] " + errorName

        msg.attach(MIMEText(message, 'plain'))

        smtp.send_message(msg)
        del msg

    smtp.quit()
