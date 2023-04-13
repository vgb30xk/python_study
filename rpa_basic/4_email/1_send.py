import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    subject = "test mail"
    body = "mail body"
    
    msg = f"subject: {subject}\n{body}"
    
    # 발신자 수신자, 정해진 형식의 메시지
    smtp.sendmail(EMAIL_ADDRESS, "vgb30xk@gmail.com", msg)