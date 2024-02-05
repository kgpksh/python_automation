import smtplib
from account import *

with smtplib.SMTP('smtp.gmail.com', 587) as smtp :
    smtp.ehlo() # 서버 상태 확인
    smtp.starttls() # 모든 내용 암호화 후 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PW) # 로그인


    # 메일 보내는 방법 1
    subject= 'test mail' # 메일 제목
    body = 'mail body' # 메일 본문

    msg = f'Subject: {subject}\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)