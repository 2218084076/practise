import logging
import random

from playwright.sync_api import Playwright, sync_playwright, expect

'''
result=[]
try{result.push(document.getElementsByClassName("detail-box-title")[0].innerText)}
catch{result.push(document.getElementsByClassName("product-info-title")[0].innerText)}
try{result.push(document.getElementsByClassName("product-name")[0].innerText)}
catch{result.push(document.getElementsByClassName("product-info-title")[0].innerText)}
try{result.push(document.getElementsByClassName("product-code-value")[0].innerText)}
catch{result.push(document.getElementsByClassName("product-info-code")[0].innerText)}
try{result.push(document.getElementsByClassName("price-now")[0].innerText)}
catch{result.push(document.getElementsByClassName("cm-price-type-sales")[0].innerText)}
cxs=document.getElementsByClassName("product-rules")
if(cxs.length==0){
    cxs=document.getElementsByClassName("promotion-item")
}
cxs_info = []
for (i=0;i<cxs.length;i++){
    cxs_info.push(cxs[i].innerText)
}
ths=document.getElementsByClassName("property-item-title")
tds=document.getElementsByClassName("property-item-value")
kv={}
for (i=0;i<ths.length;i++){
    kv[ths[i].innerText]=tds[i].innerText
}

result_info = {
    "detail-box-title":result[0],
    "product-name":result[1],
    "product-code-value":result[2],
    "price-now":result[3],
    "promotion-item":cxs_info,
    "property-item":kv,
}                
'''


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://www.cdfgsanya.com/index.html
    page.goto("http://www.cdfgsanya.com/index.html")

    # Click text=购物袋(0)您的购物袋中还没有商品搜索 >> [placeholder="护肤套装"]
    page.locator("text=购物袋(0)您的购物袋中还没有商品搜索 >> [placeholder=\"护肤套装\"]").click()

    # Fill text=购物袋(0)您的购物袋中还没有商品搜索 >> [placeholder="护肤套装"]
    page.locator('//*[@id="root"]/div/div[1]/div[3]/div/div[2]/form/div/input').fill('id')
    page.locator('//*[@id="root"]/div/div[1]/div[3]/div/div[2]/form/button').click()
    page.locator("text=购物袋(0)您的购物袋中还没有商品搜索 >> [placeholder=\"护肤套装\"]").fill("123")

    # Click text=购物袋(0)您的购物袋中还没有商品搜索 >> button
    page.locator("text=购物袋(0)您的购物袋中还没有商品搜索 >> button").click()
    # expect(page).to_have_url("http://www.cdfgsanya.com/product-list.html?sw=123")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
