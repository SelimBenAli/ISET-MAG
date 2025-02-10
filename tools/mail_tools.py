import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from tools.config_tools import ConfigTools


class MailTools:
    def __init__(self):
        self.config_tools = ConfigTools()
        self.sender_email = 'selimbenali2003@gmail.com'
        self.password = 'npzd ncfk epzc ljfj'  # Use App Password if 2FA is enabled
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.lien = "http://127.0.0.1:5000"

    def send_mail(self, receiver, subject, message):
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = receiver
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain", "utf-8"))

            # Connect to the SMTP server and send email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Secure connection
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver, msg.as_string())
            server.quit()

            print("Email sent successfully!")
            return True
        except Exception as e:
            print(f"Error: {e}")
        return False

    def get_admin_add_verification_mail_data(self):
        subject = self.config_tools.subject
        message = self.config_tools.message
        return subject, message

    def prepare_admin_add_verification_mail(self, message, mail, password):
        message = message.replace("{password}", password)
        message = message.replace("{email}", mail)
        message = message.replace('\\n', '\n')
        message = message.replace("{lien_admin}", self.lien + '/admin')
        return message

    def send_admin_add_verification_mail(self, receiver_email, receiver_pwd):
        subject, message = self.get_admin_add_verification_mail_data()
        message = self.prepare_admin_add_verification_mail(message, receiver_email, receiver_pwd)
        self.send_mail(receiver_email, subject, message)


# Usage Example
if __name__ == "__main__":
    receiver_email = "majdbmz97@gmail.com"
    receiver_pwd = "00000"
    # mailer = MailTools()
    # s, m = mailer.get_admin_add_verification_mail_data()
    # m = mailer.prepare_admin_add_verification_mail(m, receiver_email, receiver_pwd)
    # mailer.send_mail(receiver_email, s, m)
