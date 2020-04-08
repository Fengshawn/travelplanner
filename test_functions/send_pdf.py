from email.header import Header
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os


def send_mail(mail_title='test',
              attachment_pdf='D:\\py\\TravelPlanner\\test\\out.pdf',
              receiver='Write Your email'
              ):
    host_server = 'smtp.qq.com'
    sender_qq = '623654589'
    pwd = 'hdaiceqfeymhbbbc'
    sender_qq_mail = '623654589@qq.com'
    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)
    msg = MIMEMultipart('related')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)
    with open(attachment_pdf, "rb") as fp:
        fileMsg = MIMEBase('application', 'pdf')
        fileMsg.set_payload(fp.read())
        encode_base64(fileMsg)
        fileMsg.add_header('Content-Disposition', f'attachment;filename={os.path.split(attachment_pdf)[1]}')
        msg.attach(fileMsg)
    smtp.sendmail('623654589@qq.com', receiver, msg.as_string())
    smtp.quit()
    print('Success!')

if __name__ == '__main__':
    send_mail(mail_title='Details of you trip TEST')
