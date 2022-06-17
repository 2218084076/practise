import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 设置浏览器无头打开
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome(chrome_options=option)
browser = webdriver.Chrome()


def main():
    """main"""
    all_brands = get_all_brands('http://tousu.315che.com/tousulist/serial/20/')
    for i in all_brands:
        page_num = all_page_links(i)
        for j in range(1, page_num):
            p = url_string_rules(j, j)
            get_all_subpages(p)


def get_all_brands(url: str) -> list:
    l = []
    browser.get(url)
    time.sleep(random.randint(1, 3))
    div = browser.find_element(By.ID, 'letterTabList')
    a = div.find_elements(By.TAG_NAME, 'a')
    for i in a:
        brand_url = i.get_attribute('href')
        l.append(brand_url)
        print('get %s ' % brand_url)
        all_page_links(brand_url)
    return l


def get_all_subpages(home_link: str) -> list:
    """get all subpages 获取子页面 link"""
    urls_list = []
    browser.get(home_link)
    time.sleep(random.uniform(1, 3))
    a = browser.find_elements(By.CLASS_NAME, 'tousu-filter-list')[0]
    tousu_filter_list = a.find_elements(By.TAG_NAME, 'a')
    for i in tousu_filter_list:
        urls_list.append(i.get_attribute("href"))
    # print(urls_list)
    return urls_list


def all_page_links(url: str) -> int:
    """
    all page urls
    return page number
    """
    browser.get(url)
    time.sleep(random.uniform(1, 3))
    page_num = browser.find_elements(By.CLASS_NAME, 'pag-tip')[0].text.split('共')[1].split('页')[0]
    page_num = int(page_num)
    return page_num


def url_string_rules(url: str, n: int) -> str:
    """string rules"""
    t = url.split('http://tousu.315che.com/tousulist/serial/')[1]
    result_url = url.replace(url.split('http://tousu.315che.com/tousulist/serial/')[1], '%s0/0/0/%s.htm' % (t, n))
    return result_url

# print(all_page_links('http://tousu.315che.com/tousulist/serial/20/'))
