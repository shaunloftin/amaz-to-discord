# AMAZ-TO-DISCORD MONITORING
# WRITTEN BY: SHAUN LOFTIN
# github.com/shaunloftin
#
# error.py

from datetime import datetime
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def log(e):
    with open('../data/log.txt', 'a') as file:
        now = datetime.now()
        output = now.strftime("%d/%m/%Y %H:%M:%S") + ' --- ' + str(e) + '\n'
        print(output)
        file.write(output)

def err_report(e):    
    with open('../data/email_cred.txt', 'r') as file:
        SENDER = file.readline()
        USERNAME_SMTP = file.readline()
        PASSWORD_SMTP = file.readline()
    
    with open('../data/email_recipient.txt', 'r') as file:
        for email in file:
            SENDERNAME = 'DiScOrD bOt'
            RECIPIENT = email

            SUBJECT = "DiScOrD bOt StOpPeD wOrKiNg"
            BODY_TEXT = ("The bot has stopped working. Please advise. Also, hi future Shaun." + '\n' + e)
        
            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['Subject'] = SUBJECT
            msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
            msg['To'] = RECIPIENT
            # Comment or delete the next line if you are not using a configuration set
            # msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)
            
            # Record the MIME types of both parts - text/plain and text/html.
            part1 = MIMEText(BODY_TEXT, 'plain')
            part2 = MIMEText(BODY_TEXT, 'html')
            
            # Attach parts into message container.
            # According to RFC 2046, the last part of a multipart message, in this case
            # the HTML message, is best and preferred.
            msg.attach(part1)
            msg.attach(part2)
            # Try to send the message.
            try:  
                server = smtplib.SMTP("email-smtp.us-east-1.amazonaws.com", "587")
                server.ehlo()
                server.starttls()
                #stmplib docs recommend calling ehlo() before & after starttls()
                server.ehlo()
                server.login(USERNAME_SMTP, PASSWORD_SMTP)
                server.sendmail(SENDER, RECIPIENT, msg.as_string())
                server.close()
                return 0
            except Exception as e:
                return e
