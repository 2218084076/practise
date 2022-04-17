# coding=utf-8

import requests

from bs4 import BeautifulSoup

url = 'http://www.tipdm.com/'
response = requests.get(url)
print('status_code=', response.status_code)
r = response.text


def bs_for_parse(r):
    soup = BeautifulSoup(r, 'html.parser')
    ul_id = soup.find('ul', id='menu').find('a')[1]
    print(ul_id)


bs_for_parse(r)
