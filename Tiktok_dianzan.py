from selenium import webdriver
import time

def get_worksurl (share):
    share = 'http'+share.split('http')[1].split('复')[0]
    return share

share = get_worksurl(input('抖音分享地址\n'))
d=webdriver.Chrome()
d.get(share)
a=d.find_element_by_class_name('aa8946e6a10e3788dca09663eb82fc99-scss')
