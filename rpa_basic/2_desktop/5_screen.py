import pyautogui
# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 155,615 37,37,38 #252526

pixel = pyautogui.pixel(155,615)
print(pixel)

print(pyautogui.pixelMatchesColor(155, 615, (37, 37, 35)))
