import pyperclip
import pyautogui
# for w in pyautogui.getAllWindows():
#     print(w)

w = pyautogui.getWindowsWithTitle("메모장")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("JaehyunCoding", interval=0.25)
# pyautogui.write("재현코딩")

# pyautogui.write(["t", "e", "s", "t","left","left","right","l","a","enter"], interval=0.25)

# 조합키 (핫키)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
# pyautogui.hotkey("ctrl",  "a")

# pyperclip.copy("재현코딩")
# pyautogui.hotkey("ctrl", "v")


def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


my_write("마마 코딩")
