import smtplib


def mail_policy(email, text):
    gmail_user = "razzabhu@gmail.com"
    gmail_pwd = "amplitude1"
    TO = email
    SUBJECT = "Policy Details"
    TEXT = "Please find attached " + str(text) +" Policy details in email"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    BODY = '\r\n'.join(['To: %s' % TO,
            'From: %s' % gmail_user,
            'Subject: %s' % SUBJECT,
            '', TEXT])

    server.sendmail(gmail_user, [TO], BODY)

