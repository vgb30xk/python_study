import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(options=chrome_options)

browser.get("https://www.w3schools.com/")

# elem = browser.find_element(By.XPATH, '//*[@name="q"]')
# elem.send_keys("w3schools")
# elem.send_keys(Keys.ENTER)
# time.sleep(0.5)

# elem = browser.find_element(
#     By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3')
# elem.click()
# time.sleep(0.5)
elem = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[1]/a[1]')
elem.click()
time.sleep(0.5)

browser.maximize_window()

time.sleep(1)

elem = browser.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[11]')
elem.click()
time.sleep(0.5)
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[118]')
elem.click()
time.sleep(0.5)

elem = browser.find_element(By.XPATH, '//*[@id="fname"]')
time.sleep(0.5)
a = elem.send_keys("나도")
time.sleep(0.5)
elem = browser.find_element(By.XPATH, '//*[@id="lname"]')
time.sleep(0.5)
b = elem.send_keys("코딩")
time.sleep(0.5)
elem = browser.find_element(By.XPATH, '//*[@id="country"]/option[2]')
c= elem
elem.click()
time.sleep(0.5)
elem = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea')
d = elem.send_keys("퀴즈 완료하였습니다.")

time.sleep(3)
elem, c = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a')
elem.click()
time.sleep(3)
browser.quit()
print(a, b, c, d)
