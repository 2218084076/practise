import time

import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By

'''

科颜氏
https://www.cd  fgsanya.com/brand-shop.html?id=248211

阿玛尼
https://www.cdfgsanya.com/brand-shop.html?id=248148

圣罗兰
https://www.cdfgsanya.com/brand-shop.html?id=248327

赫莲娜
https://www.cdfgsanya.com/brand-shop.html?id=248226


碧欧泉
https://www.cdfgsanya.com/brand-shop.html?id=248153

植村秀
https://www.cdfgsanya.com/brand-shop.html?id=248431

欧莱雅
https://www.cdfgsanya.com/brand-shop.html?id=249511

Maison Margiela 
https://www.cdfgsanya.com/brand-shop.html?id=281265

欧珑
https://www.cdfgsanya.com/brand-shop.html?id=281031

理肤泉
https://www.cdfgsanya.com/brand-shop.html?id=248815

薇姿
https://www.cdfgsanya.com/product-list.html?sw=%E8%96%87%E5%A7%BF
'''
p = [4]
page_1 = 4
# 起始
item = 18
collection_name = 'cdf_20220701补充'

# class BrowserNow:
id_list = ['C052862', 'C053369', 'C046782', 'C046790', 'C048505',
           'C046853', 'C046847', 'C048883', 'C025219', 'C026592', 'C024387', 'C053998', 'C048264', 'C054257', 'C048270',
           'C048266', 'C056454', 'C053972', 'C049066', 'C048265', 'C049065', 'C048271', 'C048268', 'C048262', 'C056453',
           'C054258', 'C049063', 'C049064', 'C057651', 'C052074', 'C101151', 'C101150', 'C101499', 'C043952', 'C043954',
           'C043953', 'C043955', 'C055158', 'C100628', 'C055936', 'C000186']


class Browser:
    collection_name = collection_name
    prefs = {"profile.managed_default_content_settings.images": 2}

    def __init__(self):
        self.size = None
        self.db = None
        self.client = None
        self.mongo_uri = '127.0.0.1:27017'
        self.mongo_db = 'cdf'
        self.sleep = 3
        self.sku_id = None
        self.url = 'https://www.cdfgsanya.com/brands.html'
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", self.prefs)
        options.headless = True
        # options.add_argument('--proxy-server=https://218.161.32.34:8888')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.get(self.url)

    def brand_shop(self):
        """
        brand_shop
        """
        self.browser.get('https://www.cdfgsanya.com/product-list.html?sw=%s' % self.sku_id)
        time.sleep(10)
        product_item = self.browser.find_elements(By.CLASS_NAME, 'product-item-default')

        if product_item:
            product_item[0].click()
            time.sleep(2)
            self.browser.switch_to.window(self.browser.window_handles.pop())
            info_json = self.parse()
            self.mongo(info_json)
            print('The information of product %s is<%s>' % (self.sku_id, info_json.get('商品名称')))
        if not product_item:
            print('%s 没有该商品！' % self.sku_id)

    def mongo(self, info):
        """
        mongo
        :param info:
        :return:
        """
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[self.collection_name].insert_one(info)

    def mongo_close(self):
        """
        mongo close
        """
        self.client.close()

    def parse(self):
        """
        parse
        """
        try:

            detail_box_title = self.browser.find_elements(By.CLASS_NAME, 'detail-box-title')[0].text
            product_name = self.browser.find_elements(By.CLASS_NAME, 'product-name')[0].text
            product_code_value = self.browser.find_elements(By.CLASS_NAME, 'product-code-value')[0].text
            price_now = self.browser.find_elements(By.CLASS_NAME, 'product-price')[0].text
            promotion_item = self.browser.find_elements(By.CLASS_NAME, 'product-promotion')[0].text.replace('\n', '')

        except IndexError:
            detail_box_title = self.browser.find_elements(By.CLASS_NAME, 'product-name-zh')[0].text
            product_name = self.browser.find_elements(By.CLASS_NAME, 'product-name-zh')[0].text
            product_code_value = self.browser.find_elements(By.CLASS_NAME, 'product-info-code')[0].text.split('：')[1]
            price_now = self.browser.find_elements(By.CLASS_NAME, 'cm-price-type-sales')[0].text.replace('\n', '')
            promotion_item = self.browser.find_elements(By.CLASS_NAME, 'product-rules')[0].text.replace('\n', '')

        ths = self.browser.find_elements(By.CLASS_NAME, 'property-item-title')
        tds = self.browser.find_elements(By.CLASS_NAME, 'property-item-value')
        kv = {}
        for j in range(len(ths)):
            kv[ths[j].text] = tds[j].text

        if kv.get('规格：'):
            self.size = kv.get('规格：')
        if not kv.get('规格：'):
            self.size = kv.get('规格')
        info_json = {
            '品牌': detail_box_title,
            '商品名称': product_name,
            '商品编码': product_code_value,
            '当前价格': price_now,
            '商品促销': promotion_item,
            '规格': self.size,
            '详细信息': kv
        }
        return info_json

    def next_page(self):
        time.sleep(self.sleep)
        next_button = self.browser.find_elements(By.CLASS_NAME, 'cm-pagination-next')[0]
        self.browser.execute_script('arguments[0].click();', next_button)
        time.sleep(self.sleep)

    def close_browser(self):
        self.browser.quit()


if __name__ == '__main__':
    browser = Browser()
    try:
        # info in
        for i in id_list:
            browser.sku_id = i
            # browser.next_page()
            browser.brand_shop()

    except Exception as e:
        print('Exception', e)
        browser.close_browser()
