import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import xlwt


excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
table = excel.add_sheet('上海新增数据', cell_overwrite_ok=True)
info_url = 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'

def get_news_urls(info_url):
    l=[]
    options = webdriver.ChromeOptions()
    options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36')
    browser = webdriver.Chrome(chrome_options=options)
    # browser = webdriver.Chrome('C:/Users/Terry/anaconda3/Scripts/chromedriver.exe')

    time.sleep(0.5)
    browser.get(info_url)
    time.sleep(1)
    for i in range(0,24):
        url = browser.find_elements(By.CLASS_NAME,'zxxx_list')[0].find_elements(By.TAG_NAME,'a')[i]
        url = url.get_attribute('href')
        l.append(url)
        print(i)
    browser.quit()

    return l

def get_Added_daily(url):
    browser = webdriver.Chrome(r'C:\Users\Terry\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe')
    browser.minimize_window()
    time.sleep(0.5)
    browser.get(url)
    time.sleep(1)
    title = browser.find_elements(By.CLASS_NAME,'rich_media_title')[0].text
    time.sleep(0.5)
    browser.quit()
    date = title.split('（')[0]
    new_p1 = title.split('上海新增')[1].split('例本土新冠肺炎确诊病例')[0]
    new_p2 = title.split('，新增')[1].split('例本土无症状感染者')[0]
    new_p3 = title.split('本土无症状感染者，新增')[1].split('例境外输入病例')[0]
    return_json ={
        'date_time':date,
        'new_p1':new_p1,
        'new_p2':new_p2,
        'new_p3':new_p3,
    }
    print(return_json)
    return return_json

def write_to_file(n):
    json = get_Added_daily(input('微信文章链接：\n'))
    date_time = json['date_time']

    table.write(0, 0, "更新日期")
    table.write(0, 1, "本土新冠肺炎确诊病例")
    table.write(0, 2, "本土无症状感染者")
    table.write(0, 3, "境外输入")

    table.write(n,0,date_time)
    table.write(n,1,json['new_p1'])
    table.write(n,2,json['new_p2'])
    table.write(n,3,json['new_p3'])
    excel.save(r"D:\Desktop\shanghai_COVID-19--1.xls")

# for i in range(1,31):
    # write_to_file(i)
write_to_file(1)


# get_news_urls('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml')