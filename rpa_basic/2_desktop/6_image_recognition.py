import sys
import time
import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("screenshot.png")
# if trash_icon is not None:
#     pyautogui.moveTo(trash_icon)
# else:
#     print("이미지를 찾지 못했습니다.")

# for i in pyautogui.locateAllOnScreen("file_menu.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# c = pyautogui.locateOnScreen("file_menu.png")
# pyautogui.moveTo(c)

# 속도 개선
# 1. GrayScale
# c = pyautogui.locateOnScreen("file_menu.png", grayscale=True)
# pyautogui.moveTo(c)

# 2. 범위 지정
# c = pyautogui.locateOnScreen("file_menu.png", region=(991, 943, 1144-991, 1027- 943))
# pyautogui.moveTo(c)

# 3. 정확도 지정
# run_btn = pyautogui.locateOnScreen("file_menu.png", confidence=0.9)
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# f_m= pyautogui.locateOnScreen("file_menu.png")
# if f_m:
#     pyautogui.click(f_m)
# else:
#     print("발견 실패")
# while f_m is None:
#     f_m= pyautogui.locateOnScreen("file_menu.png")
#     print("발견 실패")

# pyautogui.click(f_m)
# 2. 일정 시간동안 기다리기
timeout = 5
# start = time.time()
# f_m= None
# while f_m is None:
#     f_m= pyautogui.locateOnScreen("file_menu.png")
#     end = time.time()
#     print(end)
#     if end-start > timeout:
#         print("시간 종료")
#         print(end-start)
#         sys.exit()

# pyautogui.click(f_m)


def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end-start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
        print("찾았어!!")
    else:
        print(
            f"[Timeout {timeout}s] Target not found ({img_file}). Terminate Program")
        sys.exit()

my_click("file_menu.png", 10)