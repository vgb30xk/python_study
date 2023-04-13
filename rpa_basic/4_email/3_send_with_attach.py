import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "vgb30xk@gmail.com"
msg.set_content("다운로드 하세요")

# msg.add_attachment()
with open("myw3schoolsimage.jpg", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="jpg", filename=f.name)

with open("테스트.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)
    

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)