import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_video(url):
    print("====  browser response  ====")
    driver = webdriver.Chrome('C:/Users/Terry/anaconda3/Scripts/chromedriver.exe')
    # driver.minimize_window()
    time.sleep(1)
    driver.get(url)
    print("====  get share link  ====")
    name = driver.find_elements(By.CLASS_NAME,"yy223mQ8")[0].text.split(" ")[0]
    print(name)
    v_url = driver.find_elements(By.TAG_NAME,"source")[0]
    video_url=v_url.get_attribute("src")
    aim_url = video_url
    print('download%s'%(aim_url))
    print("==== download video ====")
    aim_response = requests.get(video_url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__),'D:/Desktop/dou%s_%s.%s' % (name,time.time(), "mp4")), "ab")
    f.write(aim_response.content)
    print("====  Download successful  ====")

def analysis_works (a):
    print("==解析分享链接==")
    name = a.split(":/ ")[1].split("https")[0]
    try:
        url = 'http'+a.split('http')[1].split('复制')[0]
    except:
        url = 'http' + a.split('http')[1].split('复制')[0]
    print(url)
    return url,name

def download_img(url):
    print("== download ==")
    aim_response = requests.get(url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__),'D:/Desktop/%s.%s' % (time.time(), "jpg")), "ab")
    f.write(aim_response.content)


# 在这个文件下写的都是要用的方法,我们在本地新开一个py文件
# 这个文件都是命名的方法
'''u = analysis_works(input('抖音分享链接\n'))
print(u)
get_video(u[0],u[1])'''
