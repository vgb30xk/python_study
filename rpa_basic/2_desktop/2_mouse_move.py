import pyautogui

# 마우스 절대 좌표 이동
# pyautogui.moveTo(200, 100)
# pyautogui.moveTo(100, 200, duration=5)

# pyautogui.moveTo(100, 100, duration=0.25)
# pyautogui.moveTo(200, 200, duration=0.25)
# pyautogui.moveTo(300, 300, duration=0.25)

# 상대 좌표 이동
# pyautogui.moveTo(100, 100, duration=0.25)
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)
