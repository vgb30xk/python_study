import requests
from bs4 import BeautifulSoup

url = "https://www.lezhin.com/ko"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# rank1 = soup.find("li", attrs={"class": "gnb__item"})

webtoon = soup.find("div", text="재이미 형님")
print(webtoon)
