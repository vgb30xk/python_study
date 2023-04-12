import requests
from bs4 import BeautifulSoup

url = "https://vgb30xk.tistory.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("strong", attrs={"class": "title"})
# class 속성이 title 인 모든 "a"태그 반환
for cartoon in cartoons:
    print(cartoon.get_text())
