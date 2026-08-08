import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited_urls = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed with url: {url}")
        return
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tags = soup.find_all('a')
        urls = []
        for tag in a_tags:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        # print(urls)

        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                url_join = urljoin(url, urls2)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join, keyword)
            else:
                pass


url = input("Enter URL: ")
keyword = input("Enter keyword: ")

spider_urls(url, keyword)

# https://portswigger.net/web-security/sql-injection/cheat-sheet  ,  https://www.yahoo.com