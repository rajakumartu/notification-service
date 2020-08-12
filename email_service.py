
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SSL_PORT = 587#25,465, 587

str_test = __name__

def constuct_mail_message(toEmails, subject, text_content='', html_content='' ):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender = os.environ['AWS_MAIL_SERVER_FROM_ADDRESS']
    msg['To'] = ", ".join(toEmails)

    # Record the MIME types of both parts - text/plain and text/html.
    if text_content:
        msg.attach(MIMEText(text_content, 'plain'))
    if html_content:
        msg.attach(MIMEText(html_content, 'html'))

    return msg


def send_mail(to_emails, msg):
    username = os.environ['AWS_MAIL_SERVER_USERNAME']
    password = os.environ['AWS_MAIL_SERVER_PASSWORD']
    smtp_ssl_host = os.environ['AWS_MAIL_SERVER_HOST']
    from_email = os.environ['AWS_MAIL_SERVER_FROM_ADDRESS']

    server_connect = False
    try:
        smtp_server = smtplib.SMTP(smtp_ssl_host, SMTP_SSL_PORT)
        smtp_server.set_debuglevel(1)
        smtp_server.starttls()
        smtp_server.login(username, password)
        server_connect = True
    except Exception as e:
        print("Error ", e)
    if server_connect:
        try:
            smtp_server.sendmail(from_email, to_emails, msg.as_string())
            print("Successfully sent email")
        except Exception as e:
            print("Error: unable to send email", e)
        finally:
            smtp_server.close()

    return 'OK'


if __name__ == '__main__':
    os.environ['AWS_MAIL_SERVER_HOST'] = 'email-smtp.us-east-1.amazonaws.com'
    os.environ['AWS_MAIL_SERVER_USERNAME'] = 'AKIAZQ6ZNDCWGE3Y3QEI'
    os.environ['AWS_MAIL_SERVER_PASSWORD'] = 'BOGKaub0ThNi6jN4mFTCPv9JOQCLcpH5POdET+N6LRzJ'
    os.environ['AWS_MAIL_SERVER_FROM_ADDRESS'] = 'kokkikumar2510.3@gmail.com'

    # msg = """
    #         From: %s <%s>
    #         To: Kokki1 <kokkikumar2510.1@gmail.com>
    #         MIME-Version: 1.0
    #         Content-type: text/html
    #         Subject: SMTP HTML e-mail test
    #
    #         This is an e-mail message to be sent in HTML format
    #
    #         <b>This is HTML message.</b>
    #         <h1>This is headline.</h1>
    #     """ % ('Kokki', os.environ['AWS_MAIL_SERVER_FROM_ADDRESS'])

    # Create the body of the message (a plain-text and an HTML version).
    text_content = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html_content = """\
            <html>
              <head></head>
              <body>
                <p>Hi!<br>
                   How are you?<br>
                   Here is the <a href="http://www.python.org">link</a> you wanted.
                </p>
              </body>
            </html>
            """
    toEmails = ['kokkikumar2510.1@gmail.com', 'rajakumar.thangavelu@yahoo.co.in']
    subject = 'Test Mail Subject'
    msg = constuct_mail_message(toEmails, subject, text_content, html_content)
    send_mail(toEmails, msg)
    print(str_test)