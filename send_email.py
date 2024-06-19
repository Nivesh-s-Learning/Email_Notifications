import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

 

def send_email(to_emails, subject, body):

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = os.getenv('SMTP_USERNAME')
    password = os.getenv('SMTP_PASSWORD')
    from_email = 'sharmanivesh08@gmail.com'

    try:
        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
    
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = ', '.join(to_emails)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        # server.send_message(msg)
        server.sendmail(from_email, to_emails, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email: {str(e)}")

if __name__ == "__main__":
    to_emails = os.getenv('EMAILS')
    # Print the email addresses for log in github actions
    print(f"Sending email to: {to_emails}")
    subject = "Please commit everyday"
    body = "Please commit everyday."
    send_email(to_emails, subject, body)