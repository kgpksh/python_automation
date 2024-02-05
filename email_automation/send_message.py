import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = '테스트 메일입니다.'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
# 만약 여러명에게 메일을 보내고 싶으면 메일1, 메일2로 ', '으로 나눈 문자열을 msg['To']에 넣어야 한다.

# 참조
# msg['Cc'] = 'mail.com'

# 비밀 참조
# msg['Bcc'] = 'mail.com'


msg.set_content('테스트 본문입니다.')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PW)
    smtp.send_message(msg)