import time

import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By

'''

'''

page_num = 0
# 起始
item = 15


class Browser:
    url = 'https://www.cdfgsanya.com/brand-shop.html?id=281113'
    collection_name = 'cdf_ClédePeauBeauté肌肤之钥'
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    # options.headless = True
    options.add_argument('zh-CN,zh;q=0.9')
    options.add_argument(
        'User-Agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/102.0.5005.115 Safari/537.36"')
    firefox_options = webdriver.FirefoxOptions()

    def __init__(self):
        self.db = None
        self.client = None
        self.mongo_uri = 'localhost:27017'
        self.mongo_db = 'cdf'
        self.browser = webdriver.Chrome(chrome_options=self.options)
        self.sleep = 4
        self.browser.get(self.url)

    def brand_shop(self):
        """
        brand_shop
        """
        time.sleep(10)
        product_list = self.browser.find_elements(By.CLASS_NAME, 'product-item-default')
        print('product_list', len(product_list))
        for p in range(item, len(product_list)):
            product_list[p].click()

            time.sleep(self.sleep)
            self.browser.switch_to.window(self.browser.window_handles.pop())
            time.sleep(self.sleep)

            items = len(self.browser.find_elements(By.CLASS_NAME, 'style-normal-item'))
            colors = len(self.browser.find_elements(By.CLASS_NAME, 'style-color-item'))

            print('len(items)', items, 'len(colors)', colors)

            if items > 0:

                for n in range(items):
                    time.sleep(self.sleep)

                    self.browser.find_elements(By.CLASS_NAME, 'style-normal-item')[n].click()

                    time.sleep(self.sleep)

                    info_json = self.parse()
                    self.mongo(info_json)
                    print('page - %s-item %s - info json <%s>' % (p, n, info_json.get('product-name')))

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
                    print('page - %s-item %s - info json <%s>' % (p, c, info_json.get('product-name')))

                self.browser.close()
                self.browser.switch_to.window((self.browser.window_handles[0]))
                time.sleep(self.sleep)

            else:
                time.sleep(self.sleep)

                info_json = self.parse()

                self.mongo(info_json)
                print('page - %s-item - info json <%s>' % (p, info_json.get('product-name')))
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


browser = Browser()

if __name__ == '__main__':
    try:
        # for p in range(8):
        for page in range(page_num):
            browser.next_page()
        browser.brand_shop()
        browser.close_browser()
    except Exception as e:
        print('Exception', e)
        browser.close_browser()
