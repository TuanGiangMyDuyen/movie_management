import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class SendMail:
    def __init__(self, email_send):
        self.email = "tuanyang05@gmail.com"
        self.password = "mpqv xxje dztg ttll"
        self.email_send = email_send

    def create_mail(self, subject, body):
        self.subject = subject
        self.body = body

        # Tạo đối tượng MIMEText với mã hóa UTF-8
        self.msg = MIMEMultipart()
        self.msg['From'] = self.email
        self.msg['To'] = self.email_send
        self.msg['Subject'] = self.subject
        self.msg.attach(MIMEText(self.body, 'plain', 'utf-8'))

    def send_mail(self):
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.sendmail(self.email, self.email_send, self.msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")