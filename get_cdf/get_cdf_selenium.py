import time

import pymongo
import redis
from selenium import webdriver
from selenium.webdriver.common.by import By

"""Use selenium to crawl cdf commodity data"""
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
    'https://www.cdfgsanya.com/brand-shop.html?id=281031',
    'https://www.cdfgsanya.com/brand-shop.html?id=248153',
    'https://www.cdfgsanya.com/brand-shop.html?id=248148',  # 阿玛尼
    'https://www.cdfgsanya.com/brand-shop.html?id=248226',
    'https://www.cdfgsanya.com/brand-shop.html?id=248211',
    'https://www.cdfgsanya.com/brand-shop.html?id=248815',
    'https://www.cdfgsanya.com/lancome-product-list.html?brandType=-1&brandId=248137&categoryName=%E5%85%B0%E8%94%BB'
    '&categoryId=2900',
    'https://www.cdfgsanya.com/brand-shop.html?id=249511',
    'https://www.cdfgsanya.com/brand-shop.html?id=281265',
    'https://www.cdfgsanya.com/brand-shop.html?id=248266',
    'https://www.cdfgsanya.com/brand-shop.html?id=249144',
    'https://www.cdfgsanya.com/brand-shop.html?id=248431',
    'https://www.cdfgsanya.com/brand-shop.html?id=281030',
    'https://www.cdfgsanya.com/product-list.html?sw=VICHY',  # 薇姿
    'https://www.cdfgsanya.com/brand-shop.html?id=248327',  # YSL美妆
    'https://www.cdfgsanya.com/brand-shop.html?id=281070',  # YSL眼镜
]

collection_name = '20220822'
class_names = ['cm-image-box-img', 'item-image', 'item-link']


def save_to_redis(con: str):
    """save_to_redis"""
    redis_client = redis.from_url("redis://127.0.0.1:6379/0")
    redis_client.sadd('cdf', con)
    redis_client.client()


class Browser:
    """Browser"""
    collection_name = collection_name
    prefs = {"profile.managed_default_content_settings.images": 2}

    def __init__(self):
        self.product_list = None
        self.db = None
        self.client = None
        self.mongo_uri = '127.0.0.1:27017'
        self.mongo_db = 'cdf'
        self.sleep = 2
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("prefs", self.prefs)
        # options.headless = True
        # options.add_argument('--proxy-server=https://218.161.32.34:8888')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(
            r"C:\Users\Terry\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe", chrome_options=options)
        self.url = 'https://www.cdfgsanya.com/index.html'

    def init_browser(self):

        self.browser.get(self.url)
        time.sleep(0.5)
        pass

    def brand_shop(self):
        """
        brand_shop
        """
        time.sleep(self.sleep)
        product_list = self.get_product_list()

        print('product_list', len(product_list))
        num = 1
        for p in product_list:
            print('NO', num)
            for j in range(5):
                try:
                    if j > 1:
                        p.click()
                    time.sleep(self.sleep)
                    self.browser.execute_script("arguments[0].click();", p)
                    break
                except Exception as exc:
                    time.sleep(self.sleep + j)
                    print(f'等待 {self.sleep} No.{j} error: {exc}'.split(' (Session info: chrome')[0])
                    continue

            time.sleep(self.sleep)
            self.browser.switch_to.window(self.browser.window_handles[-1])

            time.sleep(self.sleep)

            items = len(self.browser.find_elements(By.CLASS_NAME, 'style-normal-item'))
            colors = len(self.browser.find_elements(By.CLASS_NAME, 'style-color-item'))
            try:
                style = len(self.browser.find_element(By.CLASS_NAME, 'style-list').find_elements(By.TAG_NAME, 'span'))

            except Exception as exc:
                style = -1
                print(str(exc).split(' (Session i')[0])

            print(f'items={items} colors={colors} style={style}')

            if items > 0:
                self.browser.switch_to.window(self.browser.window_handles[-1])

                for num in range(items):
                    time.sleep(self.sleep)
                    try:
                        self.browser.find_elements(By.CLASS_NAME, 'style-normal-item')[num].click()

                        time.sleep(self.sleep)

                        info_json = self.parse()
                        self.mongo(info_json)
                        print(
                            f'No.{num} The data of product is "{info_json.get("商品名称")}"'
                            f' {info_json.get("link")}')
                    except Exception as exc:
                        save_to_redis(self.browser.current_url)
                        print(f'item::::: {str(exc).split(" (Session i")[0]}')
                        continue

                self.browser.close()
                time.sleep(self.sleep)
                self.browser.switch_to.window((self.browser.window_handles[0]))

                time.sleep(self.sleep)
                continue

            if colors > 0:
                self.browser.switch_to.window(self.browser.window_handles.pop())

                for c in range(colors):
                    time.sleep(self.sleep)
                    try:
                        self.browser.find_elements(By.CLASS_NAME, 'style-color-item')[c].click()

                        time.sleep(self.sleep)
                        info_json = self.parse()
                        self.mongo(info_json)
                        print(
                            f'No.{num} The data of product {info_json.get("商品编码")} is '
                            f'"{info_json.get("商品名称")}"')
                    except Exception as exc:
                        save_to_redis(self.browser.current_url)
                        print(f'item::::: {str(exc).split(" (Session i"[0])}')
                        continue

                self.browser.close()
                self.browser.switch_to.window((self.browser.window_handles[0]))

                time.sleep(self.sleep)
                continue

            if style > 0:
                self.browser.switch_to.window(self.browser.window_handles.pop())
                for s in range(style):
                    time.sleep(self.sleep)
                    try:
                        self.browser.find_element(By.CLASS_NAME, 'style-list').find_elements(By.TAG_NAME, 'span')[
                            s].click()
                        time.sleep(self.sleep)
                        info_json = self.parse()
                        self.mongo(info_json)
                        print(
                            f'No.{num} The data of product {info_json.get("商品编码")} is '
                            f'"{info_json.get("商品名称")}"')
                    except Exception as exc:
                        save_to_redis(self.browser.current_url)
                        print(f'item::::: {str(exc).split(" (Session i")[0]}')
                        continue
                self.browser.close()
                time.sleep(self.sleep)
                self.browser.switch_to.window((self.browser.window_handles[0]))

                time.sleep(self.sleep)

            else:
                try:
                    self.browser.switch_to.window(self.browser.window_handles.pop())

                    info_json = self.parse()

                    self.mongo(info_json)
                    print(f'No.{num} The data of product {info_json.get("商品编码")} is "{info_json.get("商品名称")}"')
                    self.browser.close()
                    time.sleep(self.sleep)
                    self.browser.switch_to.window((self.browser.window_handles[0]))  # 切换主页面
                    time.sleep(self.sleep)
                except Exception as exc:
                    save_to_redis(self.browser.current_url)
                    print(self.browser.current_url, exc)
            num += 1

    def get_product_list(self):
        for class_name in class_names:
            self.product_list = self.browser.find_elements(By.CLASS_NAME, class_name)

            if self.product_list:
                print(f'class name {class_name}')
                return self.product_list
            time.sleep(self.sleep)
            continue

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
            '规格': kv.get('规格', ' '),
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
        page_number = self.browser.find_elements(By.CLASS_NAME, 'cm-pagination-number').pop().text
        return int(page_number)

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
                print(f'Page {n + 1}')
                for i in range(n):
                    browser.next_page()
                browser.brand_shop()
                time.sleep(3)
            time.sleep(5)

        browser.close_browser()
    except Exception as e:
        print('Exception', e)
        browser.close_browser()
