import json
import logging
import random

from playwright.sync_api import Playwright, sync_playwright, expect

infos = []
ids = ['C054747', 'C054750', 'C021954',
       'C022455', 'C021955', 'C021953', 'C028489', 'C053784', 'C053783', 'C046782', 'C052004', 'C052002', 'C046865',
       'C046867', 'C051888', 'C046790', 'C048505', 'C046853', 'C046864', 'C051680', 'C046847', 'C048883', 'C052038',
       'C046863', 'C054001', 'C025219', 'C028155', 'C057582', 'C055282', 'C055886', 'C055878', 'C055895', 'C055280',
       'C055879', 'C055888', 'C055882', 'C055885', 'C056064', 'C055880', 'C055883', 'C055881', 'C055884', 'C055890',
       'C055894', 'C055887', 'C055892', 'C055893', 'C055889', 'C056065', 'C055891', 'C029246', 'C029243', 'C029245',
       'C029242', 'C026592', 'C024387', 'C028072', 'C054757', 'C057133', 'C046762', 'C046756', 'C046757', 'C046759',
       'C046763', 'C053998', 'C053999', 'C037328', 'C041704', 'C041703', 'C055897', 'C057132', 'C054755', 'C048264',
       'C054257', 'C048270', 'C048263', 'C048266', 'C056454', 'C053972', 'C049066', 'C048265', 'C048267', 'C049065',
       'C048271', 'C048268', 'C048262', 'C056453', 'C054258', 'C049063', 'C049064', 'C057651', 'C046461', 'C047868',
       'C029509', 'C050550', 'C027389', 'C055962', 'C046459', 'C041442', 'C051214', 'C053318', 'C043422', 'C027398',
       'C049091', 'C039976', 'C054263', 'C054262', 'C043587', 'C036268', 'C024718', 'C024712', 'C040904', 'C043585',
       'C046485', 'C024714', 'C036278', 'C048874', 'C050083', 'C052079', 'C042840', 'C054746', 'C048645', 'C050085',
       'C050084', 'C048644', 'C042834', 'C050086', 'C044425', 'C046496', 'C042836', 'C050081', 'C050087', 'C050075',
       'C050076', 'C050077', 'C050078', 'C052075', 'C041054', 'C053786', 'C053785', 'C047857', 'C047855', 'C047859',
       'C055491', 'C055489', 'C055493', 'C055492', 'C055490', 'C024680', 'C003102', 'C024684', 'C048879', 'C030269',
       'C049535', 'C047856', 'C047858', 'C047854', 'C030425', 'C042844', 'C051887', 'C052074', 'C037663', 'C037664',
       'C050071', 'C050070', 'C037666', 'C029467', 'C053781', 'C026536', 'C026531', 'C026537', 'C049145', 'C053754',
       'C050429', 'C048875', 'C048876', 'C048877', 'C048878', 'C048880', 'C037667', 'C055156', 'C028835', 'C035234',
       'C043616', 'C050090', 'C037668', 'C053755', 'C049146', 'C035233', 'C028836', 'C052907', 'C101509', 'C101147',
       'C054570', 'C101100', 'C101693', 'C101686', 'C101694', 'C101687', 'C101151', 'C101152', 'C101150', 'C101099',
       'C101516', 'C101499', 'C043952', 'C043954', 'C101146', 'C043953', 'C043955', 'C055896', 'C100192', 'C055158',
       'C101149', 'C043607', 'C054758', 'C055899', 'C055898', 'C052652', 'C057581', 'C100628', 'C101385', 'C055154',
       'C101388', 'C101387', 'C101391', 'C101390', 'C101389', 'C029241', 'C055901', 'C047074', 'C055936', 'C038353',
       'C101393', 'C101392', 'C053317', 'C100685', 'C054774', 'C054775', 'C101384', 'C000186', 'C100623', 'C101500']


def run(page, key) -> None:
    page.wait_for_timeout(random.randint(300, 800))

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
            page.wait_for_timeout(random.randint(300, 800))
        page1 = popup_info.value
        page1.wait_for_timeout(random.randint(300, 800))
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
                '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[5]').inner_text().replace('\n', ' ')
        result_info = {
            "detail-box-title": detail_box_title,
            "product-name": product_name,
            "product-code-value": code_value,
            "price-now": price_now,
            "promotion-item": promotion_item,
            "property-item": property_item
        }
        page1.wait_for_timeout(random.randint(300, 800))
        page1.close()
        infos.append(result_info)

        print(len(infos), infos[len(infos) - 1].get('product-name'))
        with open("d:/cdf1.json", "w", encoding='utf-8') as obj:
            json.dump(infos, obj)


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.cdfgsanya.com/')
    for i in ids:
        run(page, i)
page.close()
context.close()
browser.close()
