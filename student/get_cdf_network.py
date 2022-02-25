#coding=utf-8
import json
from selenium import webdriver
from time import sleep
import xlwt
from selenium.webdriver.common.by import By
import random

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)
table.write(0,0,"序号")
table.write(0,1,"品牌")
table.write(0,2,"商品名称")
table.write(0,3,"商品编码")
table.write(0,4,"商品价格")
table.write(0,5,"商品促销")
table.write(0,6,"商品详情数据")

file_path = 'test.json'
with open(file_path,encoding='utf-8') as f:
    js = json.load(f)
    # print(js)
n=1
browser = webdriver.Chrome('C:/Users/Terry/anaconda3/Scripts/chromedriver.exe')
browser.minimize_window()

def get_info_action():
        detail_title = browser.find_elements(By.CLASS_NAME,"detail-title")[0].text
        table.write(n,1,detail_title)
        #品牌
        product_name = browser.find_elements(By.CLASS_NAME,"product-name")[0].text
        table.write(n,2,product_name)
        print(product_name)
        #商品名称
        product_code_value = browser.find_elements(By.CLASS_NAME,"product-code-value")[0].text
        table.write(n,3,product_code_value)
        #商品编码
        product_price = browser.find_elements(By.CLASS_NAME,"product-price")[0].text
        table.write(n,4,product_price)
        #商品价格
        promotion_item_wrap = browser.find_elements(By.CLASS_NAME,"promotion-item-wrap")[0].text
        table.write(n,5,promotion_item_wrap)
        #商品促销
        info = browser.find_elements(By.CLASS_NAME,"detail-tab-pro-info")[0].text.replace("\n","/")
        table.write(n,6,info)

for i in js["items"]:
    t=random.randint(1,3)
    # print("i\t",i)
    url = 'http://www.cdfgsanya.com/product.html?productId=%s&goodsId=%s&warehouseId=%s&brandId=248211'%(i["id"],i["goodsId"],i["warehouseId"])
    browser.get(url)
    sleep(t)
    table.write(n,0,n)
    # 序号
    try:
        get_info_action()
    except:
        browser.refresh() 
        sleep(2)
        get_info_action()
    #商品详情数据	
    excel.save("商品list.xls")
    print("%s\tproduct_url: "%(n),url)
    n+=1
browser.quit()