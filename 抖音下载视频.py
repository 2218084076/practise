import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_video(url,name):
    print("====下载视频====")
    driver = webdriver.Chrome('C:/Users/Terry/anaconda3/Scripts/chromedriver.exe')
    driver.minimize_window()
    time.sleep(2)
    driver.get(url)
    user_name = driver.find_elements(By.CLASS_NAME,"CjPRy13J")[0].text.replace("\n",'_')
    print(user_name)
    v_url = driver.find_elements(By.TAG_NAME,"source")[0]
    video_url=v_url.get_attribute("src")
    aim_url = video_url
    print('download%s'%(aim_url))
    print("== download ==")
    aim_response = requests.get(video_url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__),'D:/Desktop/%s_%s.%s' % (user_name,name, "mp4")), "ab")
    f.write(aim_response.content)
def analysis_works (a):
    print("==解析分享链接==")
    name = a.split(":/ ")[1].split("https")[0]
    try:
        url = 'http'+a.split('http')[1].split('复制')[0]
    except:
        url = 'http' + a.split('http')[1].split('复制')[0]
    print(url)
    return url,name

def get_img(url):
    print("== download ==")
    aim_response = requests.get(url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__),'D:/Desktop/%s.%s' % (time.time(), "jpg")), "ab")
    f.write(aim_response.content)

u = analysis_works(input('抖音分享链接\n'))
print(u)
get_video(u[0],u[1])
