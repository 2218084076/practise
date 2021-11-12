import time
import requests
import os
from selenium import webdriver
def get_video(url):
    print("====下载视频====")
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get(url)
    v_url = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[2]/video')
    f_name = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/h1')
    video_url=v_url.get_attribute("src")
    # aim_url = video_url
    print("== download ==")
    aim_response = requests.get(video_url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__),'D:/Desktop/%s.%s' % (f_name.text, "mp4")), "ab")
    f.write(aim_response.content)
    driver.quit()
def analysis_works (a):
    print("==解析分享链接==")
    url = 'http'+a.split('http')[1].split('/ ')[0]
    url=f'{url}'
    print(url)
    return url
u = analysis_works(f'{input("抖音分享文本: ")}')
get_video(u)

