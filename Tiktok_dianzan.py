from selenium import webdriver
import time
import random

'''d = webdriver.Chrome()
def get_Tiktok_url(u):
    u='http'+u.split('http')[1].split('复制')[0]
    d.get(u)
    time.sleep(20)
    for i in range(1,20):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        d.execute_script(js)
        time.sleep(2)
while True:
    get_Tiktok_url(input('抖音分享地址'))
    a = d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div[3]')
    b=a.find_element_by_class_name('_314bde61933468933fabb30f1507cdb2-scss').click()'''
key = '努力的打工人'
share = input('抖音分享地址：')
share='http'+share.split('http')[1].split('複淛')[0]
d = webdriver.Chrome()
d.get(share)
time.sleep(20)

a=d.find_elements_by_class_name('_314bde61933468933fabb30f1507cdb2-scss')
for i in range(0,501):
    a[i].click()
    time.sleep(5)
    print(i)
