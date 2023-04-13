from imap_tools import MailBox
from account import *


with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # 전체 메일 다 가져오기
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 읽지 않은 메일 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(FROM vgb30xk@gmail.com)', limit=3, reverse=True):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 어떤 글자를 포함하는 메일 (제목, 본문)
    # for msg in mailbox.fetch('(TEXT "test mail")'):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 어떤 글자를 포함하는 메일 (제목만)
    # for msg in mailbox.fetch('(SUBJECT "test mail")'):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 어떤 글자(한글)을 포함하는 메일 (제목만)
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject:
    #         print(f"[{msg.from_}] {msg.subject}")

    # 특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', reverse=True, limit=5):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 특정 날짜에 온 메일
    # for msg in mailbox.fetch('(ON 12-Apr-2023)', reverse=True, limit=5):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(ON 13-Apr-2023 SUBJECT "test mail")', reverse=True, limit=5):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 2가지 이상의 조건 중 하나라도 만족하는 메일 (또는 조건)
    for msg in mailbox.fetch('(OR ON 13-Apr-2023 SUBJECT "test mail")', reverse=True, limit=5):
        print(f"[{msg.from_}] {msg.subject}")
