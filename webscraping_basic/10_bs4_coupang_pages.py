import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
           "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

for i in range(1, 6):
    print("페이지 :", i)
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=&backgroundColor="

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:

        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            continue

        name = item.find("div", attrs={"class": "name"}).get_text()

        if "Apple" in name:
            continue

        price = item.find("strong", attrs={"class": "price-value"})
        if price == None:
            continue
        else:
            price.get_text()

        rate = item.find("em", attrs={"class": "rating"})
        if rate:
            rate = rate.get_text()
        else:
            rate = "평점 없음"
            continue

        rate_cnt = item.find(
            "span", attrs={"class": "rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            rate_cnt = "평점수 없음"
            continue

        link = item.find("a", attrs={"class": "search-product-link"})["href"]

        # 리뷰 50개 이상, 평점 4.5이상되는것만 조회
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print(f"바로가기 : {'https: // www.coupang.com'+ link}")
            print("-"*100)
