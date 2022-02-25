from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('C:/Users/Terry/anaconda3/Scripts/chromedriver.exe')
browser.get('http://www.cdfgsanya.com/product-list.html?sw=%E9%98%BF%E7%8E%9B%E5%B0%BC')
time.sleep(3)
product_list = browser.find_elements(By.CLASS_NAME,"product-item-default")

for i in product_list:
	# document.getElementsByClassName("product-item-default")[0].getElementsByTagName("a")[1]
	i.find_elements(By.TAG_NAME,"a")[1].click()
	browser.switch_to.window(browser.window_handles[1])
	time.sleep(1)
	product_name = browser.find_elements(By.CLASS_NAME,"product-name")[0].text
	print(product_name)
