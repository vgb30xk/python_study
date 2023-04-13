import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://shopping.naver.com/home")

# 무선마우스 입력
elem = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
elem.send_keys("무선마우스")
elem.send_keys(Keys.ENTER)
# 검색버튼 클릭

# 스크롤
# 지정한 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1080)')
# browser.execute_script('window.scrollTo(0, 2080)')

# 화면 가장 아래로 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
interval = 1

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    # 스크롤을 화면 가장 아래 네림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:
        break
    
    prev_height = curr_height

browser.execute_script('window.scrollTo(0, 0)')

time.sleep(2)
browser.quit()
