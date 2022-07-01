import time

import pymongo
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
brand_list = [
    # 'https://www.cdfgsanya.com/brand-shop.html?id=281031',
    'https://www.cdfgsanya.com/brand-shop.html?id=248153',
    'https://www.cdfgsanya.com/brand-shop.html?id=248148',
    'https://www.cdfgsanya.com/brand-shop.html?id=248226',
    'https://www.cdfgsanya.com/brand-shop.html?id=248211',
    'https://www.cdfgsanya.com/brand-shop.html?id=248815',
    'https://www.cdfgsanya.com/lancome-product-list.html?brandType=-1&brandId=248137&categoryName=%E5%85%B0%E8%94%BB&categoryId=2900',
    'https://www.cdfgsanya.com/brand-shop.html?id=249511',
    'https://www.cdfgsanya.com/brand-shop.html?id=281265',
    'https://www.cdfgsanya.com/brand-shop.html?id=248266',
    'https://www.cdfgsanya.com/brand-shop.html?id=249144',
    'https://www.cdfgsanya.com/brand-shop.html?id=248431',
    'https://www.cdfgsanya.com/brand-shop.html?id=281030',
    'https://www.cdfgsanya.com/product-list.html?sw=VICHY',
    'https://www.cdfgsanya.com/brand-shop.html?id=248327',  # YSL美妆
    'https://www.cdfgsanya.com/brand-shop.html?id=281070',  # YSL眼镜
    'https://www.cdfgsanya.com/brand-shop.html?id=281092'
]
p = [4]
page_1 = 4

collection_name = 'test'


# class BrowserNow:


class Browser:
    collection_name = collection_name
    prefs = {"profile.managed_default_content_settings.images": 2}

    def __init__(self):
        self.db = None
        self.client = None
        self.mongo_uri = '127.0.0.1:27017'
        self.mongo_db = 'cdf'
        self.sleep = 3
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", self.prefs)
        # options.headless = True
        # options.add_argument('--proxy-server=https://218.161.32.34:8888')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(chrome_options=options)
        self.url = 'http://www.cdfgsanya.com/index.html'

    def init_browser(self):

        self.browser.get(self.url)
        time.sleep(0.5)
        pass

    def brand_shop(self):
        """
        brand_shop
        """
        time.sleep(10)
        product_list = self.browser.find_elements(By.CLASS_NAME, 'product-item-default')
        print('product_list', len(product_list))

        for p in range(len(product_list)):

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
                    print('No.%s The data of product %s is <%s> %s' % (
                        p, info_json.get('商品编码'), info_json.get('商品名称'), info_json.get('link')))

                self.browser.close()
                time.sleep(self.sleep)
                self.browser.switch_to.window((self.browser.window_handles[0]))

                time.sleep(self.sleep)
                continue

            if colors > 0:

                for c in range(colors):
                    time.sleep(self.sleep)

                    self.browser.find_elements(By.CLASS_NAME, 'style-color-item')[c].click()

                    time.sleep(self.sleep)
                    info_json = self.parse()
                    self.mongo(info_json)
                    print('No.%s The data of product %s is <%s>' % (p, info_json.get('商品编码'), info_json.get('商品名称')))

                self.browser.close()
                self.browser.switch_to.window((self.browser.window_handles[0]))

                time.sleep(self.sleep)
                continue

            else:

                info_json = self.parse()

                self.mongo(info_json)
                print('No.%s The data of product %s is <%s>' % (p, info_json.get('商品编码'), info_json.get('商品名称')))
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
        try:
            promotion_item = self.browser.find_elements(By.CLASS_NAME, 'product-promotion')[0].text.replace('\n', '')
        except IndexError:
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

    def next_page(self):
        time.sleep(self.sleep)
        self.browser.switch_to.window(self.browser.window_handles[0])
        next_button = self.browser.find_elements(By.CLASS_NAME, 'cm-pagination-next')[0]
        self.browser.execute_script('arguments[0].click();', next_button)
        time.sleep(self.sleep)

    def get_page_num(self):
        time.sleep(self.sleep)
        page_num = self.browser.find_elements(By.CLASS_NAME, 'cm-pagination-number').pop().text
        return int(page_num)

    def close_browser(self):
        self.browser.quit()


if __name__ == '__main__':
    browser = Browser()
    try:
        for url in brand_list:
            browser.url = url
            browser.init_browser()
            page_num = browser.get_page_num()
            print('%s page for brand "%s"' % (page_num, url))
            for n in range(page_num):
                for i in range(n):
                    browser.next_page()
                browser.brand_shop()
                time.sleep(3)

        browser.close_browser()
    except Exception as e:
        print('Exception', e)
        browser.close_browser()
