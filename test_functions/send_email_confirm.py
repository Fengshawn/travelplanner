import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(recivers):
    message = MIMEText('Congratulations,Register Travel Planner Successfully.Now, you can login')  # 邮件内容
    message['From'] = 'TravelPlanner'
    message['To'] = recivers
    message['Subject'] = Header('Congratulations')
    mail = smtplib.SMTP('smtp.qq.com', 587)
    mail.login("623654589@qq.com", "hdaiceqfeymhbbbc")
    mail.sendmail("623654589@qq.com", [recivers], message.as_string())

if __name__ == '__main__':
    send_email('rzhang64@sheffield.ac.uk')

