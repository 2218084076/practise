from selenium import webdriver
from lxml import etree
from time import sleep
bro = webdriver.Chrome('C:/Users/Terry/anaconda3/Scripts/chromedriver.exe')
bro.get('http://www.cdfgsanya.com/index.html')
bro.maximize_window()
bro.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div[2]/form/div/input').clear()
bro.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div[2]/form/div/input').send_keys("科颜氏")
bro.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div[2]/form/button').click()
page_text = bro.page_source
print("page_text",page_text)

tree = etree.HTML(page_text)
name_li = []
price_li = []
li_list = tree.xpath('//*[@id="root"]/div/div[2]/div/div[4]/div/div[1]/div')

for li in li_list:
    name = li.xpath('./a/p[2]/@title')[0]
    name_li.append(name)
    price = li.xpath('./div[2]/p/span/span[2]/text()')[0]
    price_li.append(price)
sleep(5)
js="var q=document.documentElement.scrollTop=100000"
bro.execute_script(js)
sleep(2)
for i in range(3):

    bro.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[4]/div/div[2]/div/ul/li[6]').click()
    page_text = bro.page_source
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="root"]/div/div[2]/div/div[4]/div/div[1]/div')
    for li in li_list:
        name = li.xpath('./a/p[2]/@title')[0]
        name_li.append(name)
        price = li.xpath('./div[2]/p/span/span[2]/text()')[0]
        price_li.append(price)
    sleep(5)
    js = "var q=document.documentElement.scrollTop=100000"
    bro.execute_script(js)
    print(i)
print(len(name_li))
print(name_li)
print(len(price_li))
print(price_li)
sleep(5)
bro.quit()