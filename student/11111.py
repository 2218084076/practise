# import requests
# from bs4 import BeautifulSoup
# import httpx

# url = 'https://proxy.mimvp.com/freeopen?proxy=out_hp'

# r = httpx.get(url)

# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
# tr_list = soup.find_all('tr')

# for i in tr_list:
#     ip = i.find('td',class_='free-proxylist-tbl-proxy-ip')
#     country = i.find('td',class_='free-proxylist-tbl-proxy-country')
#     print(ip,country)
import json
from bs4 import BeautifulSoup
import httpx
from lxml import etree
import datetime

url1 = 'https://proxylist.geonode.com/api/proxy-list'
url_h = 'https://proxy.mimvp.com/freeopen'


def spider_json(url: str):
    now = datetime.datetime.now()
    now_time = now.strftime('%Y.%m.%d,%H:%M:%S')
    response = httpx.get(url)
    result_list = []
    page_info = response.text
    print(type(page_info))
    pagr_json = json.loads(page_info)
    print(pagr_json)
    try:
        for j in pagr_json:
            ip = j.get('ip')
            country = j.get('country_name')
            port = j.get('port')
            result_json = {
                'ip': ip,
                'country': country,
                'port': port,
                'last_check': now_time,
            }
            result_list.append(result_json)
    except AttributeError:
        pagr_json = pagr_json.get('data')
        for j in pagr_json:
            ip = j.get('ip')
            country = j.get('country_name')
            port = j.get('port')
            result_json = {
                'ip': ip,
                'country': country,
                'port': port,
                'last_check': now_time,
            }
            result_list.append(result_json)
    return result_list


def spider_html(url: str):
    r = httpx.get('https://geonode.com/free-proxy-list/')
    print(r)
    html = etree.HTML(r.text)
    tr = html.xpath('/html/body/table/tbody/tr')
    print(len(tr))
    for i in range(len(tr)):
        # /html/body/div[1]/div/div/div[1]/div/div/main/div/div[2]/div[2]/div/div[1]/div[4]/table/tbody/tr[1]/td[1]
        print(html.xpath('/html/body/table/tbody/tr[%s]/td[2]/text()' % i))
    # //*[@id="mimvp-body"]/div/table/tbody/tr[1]/td[2]




# print(spider_json(url1))
