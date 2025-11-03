import requests
from bs4 import BeautifulSoup

def get_steam_news():
    news_list = []
    url = "https://store.steampowered.com/news/"
    resp = requests.get(url)
    if resp.status_code != 200:
        return news_list

    soup = BeautifulSoup(resp.text, "lxml")
    for item in soup.select(".newsBox"):
        title = item.select_one(".newsTitle").text.strip()
        link = item.select_one("a")["href"]
        news_list.append({"title": title, "url": link})
    return news_list
