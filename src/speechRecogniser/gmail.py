import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(email_id, Text):
    fromaddr = "xyz@gmail.com"
    toaddr = email_id

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr



    # string to store the body of the mail
    body = "This is an auto-generated email \n **PLEASE DO NOT RESPOND TO THIS E-MAIL** \n \n" \
           "Please find attached policy details as requested"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    policy_name = ""
    # open the file to be sent
    if "education" in Text:
        policy_name = "Education-Reuimbursment.pdf"
    elif "appraisal" in Text:
        policy_name = "appraisal.pdf"
    elif "pto" in Text or "personal" in Text or "time off" in Text:
        policy_name = "PTO.pdf"
    filename = policy_name
    attachment = open("C:/Users\divya\Desktop\docs/" + filename, "rb")
    # storing the subject
    msg['Subject'] = "Policy Details - QA Source"
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "xyz")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


# send_email()