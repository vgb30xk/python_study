from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# limit : 최대 메일 개수
# reverse : T일 경우 최근 메일부터, F인 경우 과거메일부터
for msg in mailbox.fetch(limit=2, reverse=True):
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    # print("참조자", msg.cc)
    # print("비밀참조자", msg.bcc)
    print("날짜", msg.date)
    print("본문", msg.text)
    print("HTML 메시지", msg.html)
    print("="*100)
    
    # 첨부파일
    for att in msg.attachments:
        print("첨부파일", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)
        
        # 파일 다운로드
        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print(f"첨부 파일 {att.filename} 다운로드 완료")
            
            
mailbox.logout()
