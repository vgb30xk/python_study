from account import *
from imap_tools import MailBox

applicant_list = []

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1
    for msg in mailbox.fetch('(SENTSINCE 12-Apr-2023)'):
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print(f"순번 : {index}, 닉네임 : {nickname}, 전화번호 : {phone}")
            applicant_list.append((msg, index, nickname, phone))
            index += 1

# for applicant in applicant_list:
#     print(applicant)
