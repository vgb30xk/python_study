import requests
import re
from bs4 import BeautifulSoup


def craete_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def print_news(index, title, link):
    print(f"{index+1}. {title}")
    print(f"  (링크 : {link})")


def scrape_waether():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = craete_soup(url)
    cast = soup.find("p", attrs={"class": "summary"}).get_text()

    cur_temp = soup.find(
        "div", attrs={"class": "temperature_text"}).get_text().replace("°", "")
    min_temp = soup.find(
        "span", attrs={"class": "lowest"}).get_text().replace("°", "")
    max_temp = soup.find(
        "span", attrs={"class": "highest"}).get_text().replace("°", "")

    weather_div = soup.find("div", attrs={"class": "cell_weather"})
    am_weather = weather_div.find_all(
        "span", attrs={"class": "weather_inner"})[0]
    am_time = am_weather.find("strong", attrs={"class": "time"}).get_text()
    am_rainfall = am_weather.find(
        "span", attrs={"class": "rainfall"}).get_text()

    pm_weather = weather_div.find_all(
        "span", attrs={"class": "weather_inner"})[1]
    pm_time = pm_weather.find("strong", attrs={"class": "time"}).get_text()
    pm_rainfall = pm_weather.find(
        "span", attrs={"class": "rainfall"}).get_text()

    print(f"현재 {cast}\n{cur_temp.strip()}℃ ({min_temp}.0℃ / {max_temp}.0℃)\n{am_time} 강수확률 {am_rainfall} / {pm_time} 강수확률 {pm_rainfall}")

    dust = soup.find_all("li", attrs={"class": "item_today level1"})
    pm10 = dust[0].get_text()
    pm25 = dust[1].get_text()

    print(f"{pm10.strip()}, {pm25.strip()}")
    print()


def scrap_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.daum.net/"
    soup = craete_soup(url)
    news_list = soup.find(
        "ul", attrs={"class": "list_newsissue"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.div.div.find("a").get_text().strip()
        link = news.find("a")["href"]
        print_news(index, title, link)
    print()


def scrap_it_news():
    print("[IT 뉴스]")
    url = "https://news.daum.net/digital#1"
    soup = craete_soup(url)
    news_list = soup.find(
        "ul", attrs={"class": "list_mainnews"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.div.div.find("a").get_text().strip()
        link = news.find("a")["href"]
        print_news(index, title, link)
    print()


def scrap_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = craete_soup(url)
    sentences = soup.find_all("div", attrs={"id": re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print()

    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    print()


if __name__ == "__main__":
    scrape_waether()
    scrap_headline_news()
    scrap_it_news()
    scrap_english()
