from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)

url = "https://m-flight.naver.com/"
browser.get(url)
browser.find_element(By.XPATH, "//button[@title='한 달간 안보기']").click()

# 가는날 선택
browser.find_element(By.XPATH, "//button[contains(text(), '가는 날')]").click()

# 이번달 27일, 다음달 28일
time.sleep(0.5)
browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]').click()
time.sleep(0.5)
browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[1]').click()
time.sleep(0.5)

# 제주도 선택
browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(0.5)
browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
time.sleep(0.5)
browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]').click()
time.sleep(0.5)

# 항공권 검색
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

try:
    elem= WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]')))
    print(elem.text)
    
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div/button').click()
# print(elem)
# browser.find_element(By.XPATH, '').click()
