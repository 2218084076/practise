import logging
import time

import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By

'''

科颜氏
https://www.cdfgsanya.com/brand-shop.html?id=248211

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

page_num = 0
# 起始
item = 0
collection_name = 'cdf_220628'

logger = logging.getLogger(__name__)


class Browser:
    url = 'https://www.cdfgsanya.com/product-list.html?sw=%E8%96%87%E5%A7%BF'
    collection_name = collection_name
    prefs = {"profile.managed_default_content_settings.images": 2}

    def __init__(self):
        self.db = None
        self.client = None
        self.mongo_uri = '127.0.0.1:27017'
        self.mongo_db = 'cdf'
        self.sleep = 4
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", self.prefs)
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.get(self.url)

    def brand_shop(self):
        """
        brand_shop
        """
        self.browser.minimize_window()
        time.sleep(10)

        product_list = self.browser.find_elements(By.CLASS_NAME, 'product-item-default')
        logger.debug('product_list', len(product_list))
        for p in range(item, len(product_list)):
            product_list[p].click()

            time.sleep(self.sleep)
            self.browser.switch_to.window(self.browser.window_handles.pop())
            time.sleep(self.sleep)

            items = len(self.browser.find_elements(By.CLASS_NAME, 'style-normal-item'))
            colors = len(self.browser.find_elements(By.CLASS_NAME, 'style-color-item'))

            logger.debug('len(items)', items, 'len(colors)', colors)

            if items > 0:

                for n in range(items):
                    time.sleep(self.sleep)

                    self.browser.find_elements(By.CLASS_NAME, 'style-normal-item')[n].click()

                    time.sleep(self.sleep)

                    info_json = self.parse()
                    self.mongo(info_json)
                    logger.debug('page - %s-item %s - info json <%s>' % (p, n, info_json.get('product-name')))

                self.browser.close()
                self.browser.switch_to.window((self.browser.window_handles[0]))
                time.sleep(self.sleep)

            if colors > 0:

                for c in range(colors):
                    time.sleep(self.sleep)

                    self.browser.find_elements(By.CLASS_NAME, 'style-color-item')[c].click()

                    time.sleep(self.sleep)
                    info_json = self.parse()
                    self.mongo(info_json)
                    logger.debug('page - %s-item %s - info json <%s>' % (p, c, info_json.get('product-name')))

                self.browser.close()
                self.browser.switch_to.window((self.browser.window_handles[0]))
                time.sleep(self.sleep)

            else:
                time.sleep(self.sleep)

                info_json = self.parse()

                self.mongo(info_json)
                logger.debug('page - %s-item - info json <%s>' % (p, info_json.get('product-name')))
                self.browser.close()
                time.sleep(self.sleep)
                self.browser.switch_to.window((self.browser.window_handles[0]))  # 切换主页面
                time.sleep(self.sleep)

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

        detail_box_title = self.browser.find_elements(By.CLASS_NAME, 'detail-box-title')[0].text
        product_name = self.browser.find_elements(By.CLASS_NAME, 'product-name')[0].text
        product_code_value = self.browser.find_elements(By.CLASS_NAME, 'product-code-value')[0].text
        price_now = self.browser.find_elements(By.CLASS_NAME, 'product-price')[0].text
        promotion_item = self.browser.find_elements(By.CLASS_NAME, 'product-promotion')[0].text.replace('\n', '')
        ths = self.browser.find_elements(By.CLASS_NAME, 'property-item-title')
        tds = self.browser.find_elements(By.CLASS_NAME, 'property-item-value')
        kv = {}
        for j in range(len(ths)):
            kv[ths[j].text] = tds[j].text
        info_json = {
            'detail-box-title': detail_box_title,
            'product-name': product_name,
            'product-code-value': product_code_value,
            'price-now': price_now,
            'promotion-item': promotion_item,
            'property-item': kv
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
        for page in range(page_num):
            browser.next_page()
        browser.brand_shop()
        browser.close_browser()
    except Exception as e:
        logger.debug('Exception', e)
        browser.close_browser()
