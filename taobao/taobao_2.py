from selenium import webdriver
import time
import xlwt
import xlrd
import datetime
import random

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('taobao_page',cell_overwrite_ok=True)
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.taobao.com/?spm=a1z02.1.1581860521.1.2qUVWK')
driver.find_element_by_xpath('//*[@id="q"]').send_keys('儿童玩具')
time.sleep(2)
driver.find_element_by_class_name('search-button').click()
print('扫码登陆')
time.sleep(20)
time_now =  time.strftime('%H_%M_%S')
s=1

a = driver.find_element_by_id('mainsrp-itemlist').find_elements_by_tag_name('div')[0].find_elements_by_class_name('item')
time.sleep(5)
print(len(a))
for n in range(0,len(a)):
    t = random.randint(5,10)
    print(f"No{s}")
    time.sleep(t)
    pricea = a[n].text.split('\n')[0]
    time.sleep(t)
    table.write(s,1,pricea)
    print(pricea)
    sales = a[n].text.split('\n')[1]
    sales = sales.split('人付款')[0]
    time.sleep(t)
    table.write(s,2,sales)
    print('销量',sales)
    name = a[n].text.split('\n')[2]
    time.sleep(t)
    table.write(s,3,name)
    print(name)
    store = a[n].text.split('\n')[3]
    time.sleep(t)
    table.write(s,4,store)
    print(store)
    city = a[n].text.split('\n')[4]
    time.sleep(t)
    table.write(s,5,city)
    print(city)
    print(f'time {t}')
    excel.save(fr'D:\Terry\{time_now}.xls')
    s+=1
print(time_now)