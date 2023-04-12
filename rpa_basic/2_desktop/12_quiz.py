import pyperclip
import pyautogui
import time

pyautogui.hotkey("win",  "r")
pyautogui.write("mspaint")
pyautogui.keyDown("enter")

time.sleep(1)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
if w.isMaximized == False:
    w.maximize()

time.sleep(0.5)

c = pyautogui.locateOnScreen("test1.png", confidence=0.9)
pyautogui.click(c)
pyautogui.move(0, 300)
pyautogui.click()

pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

time.sleep(1)

pyautogui.hotkey("alt", "f4")

time.sleep(0.5)

c = pyautogui.locateOnScreen("test2.png", confidence=0.77)
pyautogui.click(c)
