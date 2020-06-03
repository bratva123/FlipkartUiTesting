import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMail(recieverMail="lavkr0403@gmail.com"):
    senderEmail = "lavkr0403@gmail.com"
    receiverEmail = recieverMail
    password = "nishi\"123"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = senderEmail
    message["To"] = recieverMail

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,\n
    Sending Report of tests\n
    Please Find the attachment"""


    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)



    #adding attachment to the mail

    # open the file to be sent
    filename1 = "report.html"
    filename2 = "automation.log"

    attachment1 = open("/home/global/Desktop/FlipkartUiTesting/reports_and_log/report.html", "rb")
    attachment2 = open("/home/global/Desktop/FlipkartUiTesting/reports_and_log/automation.log", "rb")

    # instance of MIMEBase and named as p
    p1 = MIMEBase('application', 'octet-stream')
    p2 = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p1.set_payload((attachment1).read())
    p2.set_payload((attachment2).read())

    # encode into base64
    encoders.encode_base64(p1)
    encoders.encode_base64(p2)
    p1.add_header('Content-Disposition', "attachment1; filename= %s" % filename1)
    p2.add_header('Content-Disposition', "attachment2; filename= %s" % filename2)
    message.attach(p1)
    message.attach(p2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(senderEmail, password)
        server.sendmail(
            senderEmail, recieverMail, message.as_string()
        )