import smtplib
import os
from dotenv import load_dotenv
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

# Load env vars
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
MY_ADDRESS = os.getenv("MY_ADDRESS")
PASSWORD = os.getenv("PASSWORD")
HOST= os.getenv("HOST")
PORT=os.getenv("PORT")

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def get_matches(names):
    """
    Return a dict of matches from a list of names.
    """
    names_copy = names.copy()
    random.shuffle(names_copy)
    matches = [names_copy[i-1] for i in range(len(names_copy))]
    matches_dict = {}
    for i in range(len(names_copy)):
        matches_dict[names_copy[i]] = matches[i]
    return matches_dict

def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('docs/contacts.txt') # read contacts
    matches = get_matches(names)
    message_template = read_template('docs/message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(HOST, PORT)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message
        gives_to = matches[name] # Find out match

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title(), GIVES_TO=gives_to.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Secret 🎅"

        # add in the message body
        msg.attach(MIMEText(message, 'html'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()
