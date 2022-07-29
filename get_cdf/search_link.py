"""Search link"""
import time

import pymongo
import redis
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Atelier Cologne
BIOTHERM
GIORGIO ARMANI
HR
KIEHLS
LA ROCHE POSAY
LANCOME
LOREAL
Maison Margiela
PRADA
RALPH LAUREN
SHU UEMURA
SKINCEUTICALS
VICHY
YSL
'''

collection_name = '20220721'
lost_link=['https://www.cdfgsanya.com/product.html?productId=497341&goodsId=617784&warehouseId=10',
           ]

def save_to_redis(con: str):
    """save_to_redis"""
    redis_client = redis.from_url("redis://127.0.0.1:6379/0")
    redis_client.sadd('cdf', con)
    redis_client.client()


def read_from_redis():
    """read from redis"""
    redis_client = redis.from_url("redis://127.0.0.1:6379/0")
    values = redis_client.smembers('cdf')
    return values


class Browser:
    """Browser"""
    collection_name = collection_name
    prefs = {"profile.managed_default_content_settings.images": 2}

    def __init__(self):
        self.db = None
        self.client = None
        self.mongo_uri = '127.0.0.1:27017'
        self.mongo_db = 'cdf'
        self.sleep = 3
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("prefs", self.prefs)
        # options.headless = True
        # options.add_argument('--proxy-server=https://218.161.32.34:8888')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(chrome_options=options)
        self.url = 'https://www.cdfgsanya.com/index.html'

    def init_browser(self):
        """init_browser"""
        self.browser.get(self.url)
        time.sleep(0.5)

    def brand_shop(self):
        """
        brand_shop
        """
        time.sleep(10)

        try:
            info_json = self.parse()

            self.mongo(info_json)
            print('The data of product %s is <%s> %s' % (
                info_json.get('商品编码'), info_json.get('商品名称'), info_json.get('link')))

            time.sleep(self.sleep)

        except Exception as exc:
            save_to_redis(self.browser.current_url)
            print(self.browser.current_url, exc)

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
        """parse"""
        try:
            detail_box_title = self.browser.find_elements(By.CLASS_NAME, 'detail-box-title')[0].text
        except IndexError:
            detail_box_title = self.browser.find_elements(By.CLASS_NAME, 'product-name-zh')[0].text

        try:
            product_name = self.browser.find_elements(By.CLASS_NAME, 'product-name')[0].text
        except IndexError:
            product_name = self.browser.find_elements(By.CLASS_NAME, 'product-name-zh')[0].text

        try:
            product_code_value = self.browser.find_elements(By.CLASS_NAME, 'product-code-value')[0].text
        except IndexError:
            product_code_value = self.browser.find_elements(By.CLASS_NAME, 'product-info-code')[0].text.split('：')[1]

        try:
            price_now = self.browser.find_elements(By.CLASS_NAME, 'product-price')[0].text
        except IndexError:
            price_now = self.browser.find_elements(By.CLASS_NAME, 'price-item')[0].text

        try:
            promotion_item = self.browser.find_elements(By.CLASS_NAME, 'product-promotion')[0].text.replace('\n', '')
        except IndexError:
            promotion_item = self.browser.find_elements(By.CLASS_NAME, 'product-rules')[0].text.replace('\n', '')
        else:
            promotion_item = ''

        ths = self.browser.find_elements(By.CLASS_NAME, 'property-item-title')
        tds = self.browser.find_elements(By.CLASS_NAME, 'property-item-value')
        kv = {}
        for j in range(len(ths)):
            kv[ths[j].text] = tds[j].text
        info_json = {
            '品牌': detail_box_title,
            '商品名称': product_name,
            '商品编码': product_code_value,
            '当前价格': price_now,
            '商品促销': promotion_item,
            '规格': kv.get('规格'),
            '详细信息': kv,
            'link': self.browser.current_url
        }
        return info_json

    def close_browser(self):
        self.browser.quit()


# brand_list = read_from_redis()
# print(brand_list)
if __name__ == '__main__':
    brand_list = read_from_redis()
    browser = Browser()
    try:
        for url in brand_list:
            browser.url = str(url).split("'")[1]
            browser.init_browser()
            browser.brand_shop()
            time.sleep(3)

    except Exception as e:
        print('Exception', e)
        browser.close_browser()
