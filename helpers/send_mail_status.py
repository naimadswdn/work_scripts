import smtplib


def send_email_status(sender, receiver, topic, message, status='GREEN'):

    message = """From: VALHALLA <VALHALLA@xxx.com>
To: {}
MIME-Version: 1.0
Content-type: text/html
Subject: {}: {}

{}
""".format(receiver, status, topic, message)


    try:
        smtpObj = smtplib.SMTP('xxx')
        smtpObj.sendmail(sender, receiver, message)
        print("Successfully sent email")
    except SMTPException:
        print("Error: unable to send email")
