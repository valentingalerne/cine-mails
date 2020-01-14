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
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def send(error):
    config = configparser.ConfigParser()
    config.read('./address.ini')

    ADDRESS = config['data_address']['address']
    PASSWORD = config['data_address']['password']

    names, emails = get_contacts('./files/address.txt')
    message_template = read_template('./files/template.txt')

    smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtp.starttls()
    smtp.login(ADDRESS, PASSWORD)

    for name, email in zip(names, emails):
        msg = MIMEMultipart()

        message = message_template.substitute(NUM_ERROR=str(error))
        print(name)
        print(message)

        msg['From'] = ADDRESS
        msg['To'] = email
        msg['Subject'] = "[Erreur] une erreur est survenue"

        msg.attach(MIMEText(message, 'plain'))

        smtp.send_message(msg)
        del msg

    smtp.quit()
