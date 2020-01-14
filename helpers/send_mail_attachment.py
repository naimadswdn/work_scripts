import smtplib
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


def send_mail(sender, receivers, subject, message, files=[]):
    """Compose and send email with provided info and attachments.

    Args:
        sender (str): from name
        receivers (str): to name; comma separated string i.e. 'xyz@xxx.com,abc@xxx.com'
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
    """
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receivers
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(op.basename(path)))
        msg.attach(part)

    smtp = smtplib.SMTP('HHHHUB02.DKD1.ROOT4.NET')
    smtp.sendmail(sender, receivers.split(','), msg.as_string())
    smtp.quit()
