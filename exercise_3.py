import os
import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"


class WorkingWithMail:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def sending_letter(self, recipients, subject, message_text):
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = self.login
        message['To'] = ', '.join(recipients)
        message.attach(MIMEText(message_text))
        server = smtplib.SMTP(GMAIL_SMTP, 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.login, self.password)
        server.sendmail(self.login, recipients, message.as_string())
        server.quit()

    def receiving_letters(self):
        header = None
        imap_server = imaplib.IMAP4_SSL(GMAIL_IMAP)
        imap_server.login(self.login, self.password)
        imap_server.list()
        imap_server.select("INBOX")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = imap_server.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = imap_server.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        imap_server.logout()
        return email_message


if __name__ == '__main__':
    working_mail = WorkingWithMail(LOGIN, PASSWORD)
    subject_test = 'Subject'
    message_test = 'Message'
    recipients_test = ['vasya@email.com', 'petya@email.com']
    working_mail.sending_letter(recipients_test, subject_test, message_test)
    working_mail.receiving_letters()
