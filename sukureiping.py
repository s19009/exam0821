from bs4 import BeautifulSoup
import requests
import codecs


url = "https://kamigame.jp/%E3%83%89%E3%83%A9%E3%82%AF%E3%82%A811/%E3%83%A2%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%BC/index.html"

HTML = requests.get(url)
HTML.encoding = HTML.apparent_encoding

SOUP = BeautifulSoup(HTML.text, 'html.parser')

for i in SOUP.select("tbody"):
    for a in i.select("tr"):
        with open('file.txt', 'w') as f:
            print(SOUP.select("tbody"), file=f)
