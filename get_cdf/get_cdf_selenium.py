from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xlwt
import random

driver = webdriver.Chrome()
excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)

url = 'http://www.cdfgsanya.com/product-list.html?sw=Margiela'

driver.get(url)

