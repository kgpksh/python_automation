import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = '테스트 메일입니다.'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('다운로드 하세요.')

with open('email_automation/attachment_test.txt', 'rb') as f :
    msg.add_attachment(f.read(), maintype='text', subtype='plain', filename = f.name)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PW)
    smtp.send_message(msg)