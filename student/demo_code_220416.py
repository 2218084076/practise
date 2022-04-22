# coding=utf-8
"""demo Internet worm"""

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import json


def browser_reaction(url: str):
    print("==== browser_reaction ====")
    l1 = []
    l2 = []
    ca = DesiredCapabilities.CHROME
    ca['goog:loggingPrefs'] = {"performance": "ALL"}
    browser = webdriver.Chrome("C:/Users/Terry/AppData/Local/Programs/Python/Python310/Scripts/chromedriver.exe")
    browser.get(url)
    time.sleep(3)
    print('web info', browser.get_log('performance')[2])
    u = browser.find_element(By.ID, 'getButtonBoxLink').get_attribute('href')
    print(u)
    browser.get(u)
    time.sleep(4)
    name_list = browser.find_elements(By.CLASS_NAME, 'overflow-wrap')
    price_list = browser.find_elements(By.CLASS_NAME, 'main-price')
    for i, j in zip(name_list, price_list):
        l1.append(i.text)
        l2.append(j.text)
    browser.quit()
    return l1, l2


def write_json_file(l1, l2):
    print("==== write_json_file ====")
    result_list = []
    for n, m in zip(l1, l2):
        result_json = {
            'name': n,
            'price': m
        }
        result_list.append(result_json)
    result_list_n = json.dumps(result_list)
    print(result_list_n)
    # f = open('new_json.json', 'w')
    # f.write(result_list_n)
    # f.close()


now = browser_reaction('http://tipdm.com/')
write_json_file(now[0], now[1])
