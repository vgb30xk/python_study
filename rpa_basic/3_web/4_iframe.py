import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()

browser.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '//*[@id="html"]')

elem.click()

time.sleep(1)

browser.switch_to.default_content()

elem = browser.find_element(By.XPATH, '//*[@id="html"]')

elem.click()

time.sleep(3)

browser.quit()
