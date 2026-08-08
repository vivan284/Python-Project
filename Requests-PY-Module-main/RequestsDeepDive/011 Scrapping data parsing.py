import os
from bs4 import BeautifulSoup

for file in os.listdir("htmls"):
    with open(f"htmls/{file}", encoding="utf-8") as f:
        htmlContent = f.read()
        soup = BeautifulSoup(htmlContent,"html.parser")
        for link in soup.find_all("a"):
            print(link.get("href"))

