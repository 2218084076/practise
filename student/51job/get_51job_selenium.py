"""get 51job"""
import json
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

proxy_list = ['121.37.31.195', '120.42.46.226', '218.1.200.202', '210.5.10.87', '118.193.47.193', '175.24.112.3',
              '124.156.100.83', '58.220.95.40', '117.34.25.11', '116.63.170.189', '98.162.96.41', '98.170.57.231',
              '95.43.42.100', '193.84.184.25', '94.26.108.67', '93.184.151.48', '193.163.116.29']

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome()


def get_all_pos_page(url: str) -> list:
    browser.get(url)
    time.sleep(random.randint(3, 10))
    items = []
    position_list = browser.find_elements(By.CLASS_NAME, 'job_item')
    for p in position_list:
        items.append(p.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href'))
    print(items)
    return items


def parse_item(items: list) -> list:
    result_list = []
    for i in items:
        browser.get(i)
        time.sleep(random.randint(4, 8))
        pos_title = browser.find_elements(By.CLASS_NAME, 'pos_title')[0].text  # 岗位名称
        pos_address = browser.find_elements(By.CLASS_NAME, 'pos_address')[0].text  # 工作地址（城市）
        posdes = browser.find_elements(By.CLASS_NAME, 'posDes')[0].text.replace('\n', '')  # 职位介绍
        try:
            item_condition = browser.find_elements(By.CLASS_NAME, 'item_condition')[0].text  # 人数

        except:
            item_condition = ''
        pos_salary = browser.find_elements(By.CLASS_NAME, 'pos_salary')[0].text  # 薪资
        base_info = browser.find_elements(By.CLASS_NAME, 'baseInfo_link')[0].text  # 公司名称
        industry = browser.find_elements(By.CLASS_NAME, 'comp_baseInfo_belong')[0].text  # 补充说明（所在行业分类）
        area = browser.find_elements(By.CLASS_NAME, 'pos-area')[0].text  # 详细地址
        result_json = {
            'pos_title': pos_title,
            'pos_address': pos_address,
            'posdes': posdes,
            'item_condition': item_condition,
            'pos_salary': pos_salary,
            'base_info': base_info,
            'industry': industry,
            'area': area,
        }
        result_list.append(result_json)
        print(result_json)
    return result_list


def write_json_file(result_list: list):
    with open('58_job.json', 'w', encoding='utf-8') as f:
        json.dump(result_list, f)


page_num = 1
while page_num < 3500:
    url = 'https://sh.58.com/job/pn%s/' % page_num
    print('This is page-%s-%s' % (page_num, url))
    browser.get(url)
    time.sleep(random.randint(3, 10))
    items = []
    position_list = browser.find_elements(By.CLASS_NAME, 'job_item')
    for p in position_list:
        items.append(p.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href'))

    all_pos_pages = get_all_pos_page(url)
    items_list = parse_item(all_pos_pages)
    write_json_file(items_list)
    page_num += 1

browser.quit()
