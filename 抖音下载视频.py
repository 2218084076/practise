import time
import requests
import os
from selenium import webdriver
def get_video(url):
    print("====下载视频====")
    driver = webdriver.Chrome()
    driver.get(url)
    v_url = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[2]/video')
    video_url=v_url.get_attribute("src")
    # aim_url = video_url
    print("== download ==")
    aim_response = requests.get(video_url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__),'D:/Desktop/%s.%s' % (time.time(), "mp4")), "ab")
    f.write(aim_response.content)
def analysis_works (a):
    print("==解析分享链接==")
    url = 'http'+a.split('http')[1].split('複制')[0]
    url=f'{url}'
    print(url)
    return url
u = analysis_works('8.71 hBG:/ %东北妈妈穿啥 冬季篇，张喽张喽给家长买点衣服过冬！！！  https://v.douyin.com/Rda7ryq/ 複制此链接，打開Dou荫搜索，直接观看视頻！')
get_video(u)
