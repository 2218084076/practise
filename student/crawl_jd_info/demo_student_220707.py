import requests
from bs4 import BeautifulSoup
from lxml import etree

url = "https://mall.jd.com/index-811875.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"}
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
text = res.text
soup = BeautifulSoup(text, "lxml")

title_list = soup.find_all('div',class_='jDesc'))
price_list =

