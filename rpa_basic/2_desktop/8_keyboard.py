import pyautogui
# for w in pyautogui.getAllWindows():
#     print(w)

w = pyautogui.getWindowsWithTitle("메모장")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("JaehyunCoding", interval=0.25)
# pyautogui.write("재현코딩")

# pyautogui.write(["t", "e", "s", "t","left","left","right","l","a","enter"], interval=0.25)

