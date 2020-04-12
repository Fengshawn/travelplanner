"""
@author:ZRM
@file:qq_send.py
@time:2020/03/29
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#
# msg_from = '623654589@qq.com'  # 发送方邮箱
# passwd = 'hdaiceqfeymhbbbc'
#           hdaiceqfeymhbbbc填入发送方邮箱的授权码
# msg_to = 'rzhang64@sheffield.ac.uk'  # 收件人邮箱
#
# body = '''
#    #this is flight inforamtion
#
#    #this is hotel informaiton
#
#    #this is attractions infroamtion
#
#    '''
# msg = MIMEText(body)
# msg['Subject'] = 'Travel Planner'
# msg['From'] = msg_from
# msg['To'] = msg_to
#
# s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
# s.login(msg_from, passwd)
# s.sendmail(msg_from, msg_to, msg.as_string())
# s.quit()
# if __name__ == "__main__":
#     pass

def send_email(toAddr):
    fromAddr = '623654589@qq.com'
    mypass = 'hdaiceqfeymhbbbc'
    msg = MIMEMultipart()
    msg['From'] = fromAddr
    msg['to'] = toAddr
    msg['Subject'] = 'Travel Planner'
    body = '''
    #this is flight inforamtion

    #this is hotel informaiton

    #this is attractions infroamtion

    '''
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(fromAddr, mypass)
    server.sendmail(fromAddr, toAddr, msg.as_string())

    server.quit()
send_email("rzhang64@sheffield.ac.uk")