import smtplib
from account import *
from imap_tools import MailBox
from email.message import EmailMessage

max_val = 3
applicant_list = []

print("[1. 지원자 메일 조회]")
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1
    for msg in mailbox.fetch('(SENTSINCE 12-Apr-2023)'):
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            # print(f"순번 : {index}, 닉네임 : {nickname}, 전화번호 : {phone}")
            applicant_list.append((msg, index, nickname, phone))
            index += 1

print("[2. 선정 / 탈락 메일 발송]")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for applicant in applicant_list:
        to_addr = applicant[0].from_
        # index = applicant[1]
        # nickname = applicant[2]
        # phone = applicant[3]
        index, nickname, phone = applicant[1:]

        title = None
        content = None

        if index <= max_val:
            title = "파이썬 특강 안내 [선정]"
            content = f"{nickname}님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 {index}번)"
        else:
            title = "파이썬 특강 안내 [탈락]"
            content = f"{nickname}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {index - max_val}번)"

        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname, "님에게 메일 발송 완료")
