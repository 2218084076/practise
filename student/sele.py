from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# option = webdriver.ChromeOptions()
# option.add_argument("headless")
# browser = webdriver.Chrome(chrome_options=option)
browser = webdriver.Chrome()

browser.get('http://tousu.315che.com/tousulist/serial/20/')


# /html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[1]
def get_all_subpages(home_link: str) -> list:
    """get all subpages"""
    urls_list = []
    browser.get(home_link)
    time.sleep(random.uniform(1, 3))
    a = browser.find_elements(By.CLASS_NAME, 'tousu-filter-list')[0]
    tousu_filter_list = a.find_elements(By.TAG_NAME, 'a')
    for i in tousu_filter_list:
        urls_list.append(i.get_attribute("href"))
    # print(urls_list)
    return urls_list


def all_page_links(url: str) -> None:
    """all page urls"""
    browser.get(url)
    time.sleep(random.uniform(1, 3))
    page_num = browser.find_elements(By.CLASS_NAME, 'pag-tip')[0].text.split('共')[1].split('页')[0]
    page_num = int(page_num)
    for n in range(1, page_num + 1):
        p = url_string_rules(url, n)
        get_all_subpages(p)


def url_string_rules(url: str, n: int) -> str:
    """string rules"""
    t = url.split('http://tousu.315che.com/tousulist/serial/')[1]
    result_url = url.replace(url.split('http://tousu.315che.com/tousulist/serial/')[1], '%s0/0/0/%s.htm' % (t, n))
    return result_url

# print(all_page_links('http://tousu.315che.com/tousulist/serial/20/'))
