import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(
    "https://www.w3schools.com/tags/att_input_type_radio.asp")
curr_handle = browser.current_window_handle
print("ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ", curr_handle)

browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles
for handle in handles:
    print(handle)
    browser.switch_to.window(handle)
    print(browser.title)
    print()

# 새로 이동된 브라우저에서 뭔가 자동화 작업을 수행

# 그 부라우저를 종료
print("현재 핸들 닫기")
browser.close()

# 이전핸들로 돌아오기
print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)

print(browser.title)

time.sleep(2)

browser.get('http://daum.net')

time.sleep(3)
browser.quit()
