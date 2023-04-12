import time
from PIL import ImageGrab

time.sleep(5)

for i in range(1, 11):
    img = ImageGrab.grab()
    img.save(f"image{i}.png")
    time.sleep(2)