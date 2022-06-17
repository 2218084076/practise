"""通过商品id查找"""
import json
import logging
import random
import time

from playwright.sync_api import Playwright, sync_playwright, expect

infos = []
ids = ['C055940', 'C055941', 'C055942', 'C055943', 'C055944', 'C018863', 'C026741', 'C051162', 'C040267', 'C040268',
       'C040269', 'C040270', 'C040308', 'C041295', 'C000569', 'C045059', 'C100560', 'C100563', 'C049703', 'C049704',
       'C049909', 'C055022', 'C054759', 'C044695', 'C045062', 'C015874', 'C051161', 'C049544', 'C049545', 'C049546',
       'C000278', 'C045281', 'C056395', 'C051443', 'C049105', 'C053752', 'C053316', 'C033525', 'C037234', 'C043950',
       'C051622', 'C000277', 'C054897', 'C051620', 'C053307', 'C055158', 'C044264', 'C049693', 'C051160', 'C045061',
       'C046457aq', 'C027725', 'C044761', 'C034756', 'C044292', 'C051159', 'C043953', 'C043955', 'C053314', 'C046455',
       'C043952', 'C043954', 'C055947', 'C039090', 'C046904', 'C026594', 'C046905', 'C045470', 'C043952', 'C043954',
       'C043953', 'C055158', 'C055936']


def run(page, key) -> None:
    page.wait_for_timeout(random.randint(500, 1800))

    if '404' in page.title():
        page.reload()
        page.wait_for_timeout(random.randint(500, 1500))
    page.locator('//*[@id="root"]/div/div[1]/div[3]/div/div[2]/form/div/input').fill('%s' % key)
    page.wait_for_timeout(random.randint(100, 300))

    page.locator('//*[@id="root"]/div/div[1]/div[3]/div/div[2]/form/button').click()
    page.wait_for_timeout(random.randint(300, 800))

    print('  Find %s Get <%s>' % (key, page.url))
    if '404' in page.title():
        page.reload()
        page.wait_for_timeout(random.randint(500, 1500))

    if '没有符合条件的商品' in page.locator('//*[@id="root"]/div/div[2]/div').inner_text().replace('\n', ''):
        print('Error 商品不存在 <%s> Get <%s>' % (key, page.url))
        return None
    else:
        with page.expect_popup() as popup_info:
            page.locator('//*[@id="root"]/div/div[2]/div/div[4]/div/div[1]/div/div[1]/a/img').click()
            page.wait_for_timeout(random.randint(500, 1500))
        page1 = popup_info.value
        page1.wait_for_timeout(random.randint(500, 1500))

        try:
            detail_box_title = page1.locator(
                '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div').inner_text()
        except:
            detail_box_title = page1.locator(
                '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/ul/li[3]/span[2]').inner_text()
        property_item = page1.evaluate('''
a = function() {
ths=document.getElementsByClassName("property-item-title")
tds=document.getElementsByClassName("property-item-value")
kv={}
for (i=0;i<ths.length;i++){
    kv[ths[i].innerText]=tds[i].innerText
}
return kv
}
        ''')
        try:
            product_name = page1.evaluate('document.getElementsByClassName("product-name")[0].innerText')
        except:
            product_name = page1.evaluate('document.getElementsByClassName("product-info-title")[0].innerText')
        try:
            code_value = page1.locator(
                '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/span[2]').inner_text()
        except:
            code_value = page1.evaluate('document.getElementsByClassName("product-code-value")[0].innerText')
        try:
            price_now = page1.evaluate('document.getElementsByClassName("price-now")[0].innerText')
        except:
            price_now = page1.locator(
                '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div').inner_text()
        try:
            promotion_item = page1.evaluate(
                'document.getElementsByClassName("promotion-item-wrap")[0].innerText').replace('\n', ' ')
        except:
            promotion_item = page1.locator(
                '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[2]').inner_text().replace('\n',
                                                                                                                 ' ')
        result_info = {
            "detail-box-title": detail_box_title,
            "product-name": product_name,
            "product-code-value": code_value,
            "price-now": price_now,
            "promotion-item": promotion_item,
            "property-item": property_item
        }
        time.sleep(random.randint(5, 10))
        page1.wait_for_timeout(random.randint(500, 1500))
        page1.close()
        infos.append(result_info)

        print(len(infos), infos[len(infos) - 1].get('product-name'))
        with open("d:/cdf-%s.json" % (time.strftime('%Y-%m-%d', time.localtime())), "w", encoding='utf-8') as obj:
            json.dump(infos, obj)


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.cdfgsanya.com/')
    for i in ids:
        run(page, i)
page.close()
context.close()
browser.close()
