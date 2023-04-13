import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/default.asp')
browser.maximize_window()
time.sleep(2)

# 특정 영역 스크롤
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[64]')

# ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 좌표 정보 이용
# xy = elem.location_once_scrolled_into_view
# print("type : ", type(xy))
# print("value : ", xy)

elem.click()

time.sleep(5)
browser.quit()