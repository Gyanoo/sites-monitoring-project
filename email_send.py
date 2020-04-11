import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:
    def __init__(self, email_to, subject, link):
        massageHTML = '<h1>Changes were found</h1> <p>To check click <a href="' + link + '">here<a><p>'
        massagePlain = 'Changes were found To check click here'
        message = MIMEMultipart('alternative')
        message['From'] = 'my.pro9ram@gmail.com'
        message['To'] = email_to
        message['Subject'] = subject

        message.attach(MIMEText(massagePlain, 'plain'))
        message.attach(MIMEText(massageHTML, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('my.pro9ram@gmail.com', '<myProgram>')
        text = message.as_string()
        server.sendmail('my.pro9ram@gmail.com', email_to, text)
        server.close()

