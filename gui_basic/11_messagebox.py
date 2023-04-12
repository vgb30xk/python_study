import tkinter.messagebox as msbox
from tkinter import *

root = Tk()
root.title("Jahyun GUI")
root.geometry("640x480")

# 기차 예매 시스템이라 가정


def info():
    msbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")


def warn():
    msbox.showwarning("경고", "해당 좌석은 매진되었습니다.")


def error():
    msbox.showerror("에러", "결제 오류가 발생되었습니다.")


def okcancel():
    msbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")


def retrycancel():
    response = msbox.askretrycancel("재시도 / 취소", "일시적 오류입니다. 다시 시도하시겠습니까?")
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")


def yesno():
    msbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 다시 시도하시겠습니까?")


def yesnocancel():
    response = msbox.askyesnocancel(
        title=None, message="에매 내역이 저장되지 않았습니다.\n저장 후 예매하시겠습니까?")

    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")


Button(root, text="알림", command=info).pack()
Button(root, text="경고", command=warn).pack()
Button(root, text="에러", command=error).pack()

Button(root, text="확인 취소", command=okcancel).pack()
Button(root, text="재시도 취소", command=retrycancel).pack()
Button(root, text="예 아니오", command=yesno).pack()
Button(root, text="예 아니오 취소", command=yesnocancel).pack()

root.mainloop()
