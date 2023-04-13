import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '//*[@id="html"]')

if elem.is_selected() == False:
    print("선택 안되어있어서 선택함")
    elem.click()
else:
    print("선택 되어있으므로 아무것도 안함")
# //*[@id="html"]

time.sleep(2)

if elem.is_selected() == False:
    print("선택 안되어있어서 선택함")
    elem.click()
else:
    print("선택 되어있으므로 아무것도 안함")
# //*[@id="html"]


browser.quit()
