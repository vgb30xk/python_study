import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "vgb30xk@gmail.com"

# 여러명에게 보낼때
# msg["To"] = "xxxx@xxx.com, xxxx@xxx.com, xxxx@xxx.com"
# to_list = ["vgb30xk@naver.com, vgb30xk@gmail.com"]
# msg["To"] = ", ".join(to_list)

# # 참조
# msg["Cc"] = "vgb30xk@naver.com"

# # 비밀참조
# msg["Bcc"] = "vgb30xk@naver.com"

msg.set_content("테스트 본문입니다")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
