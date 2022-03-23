from selenium import webdriver
import time
from selenium.webdriver.common.by import By
browser=webdriver.ChromeOptions()
browser.add_argument('User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36')
browser = webdriver.Chrome('C:/Users/Terry/anaconda3/Scripts/chromedriver.exe')
cookies = {
    'value':'547ce18ac2073c1a45aa5821e5b1f052',
    'name' :'security_session_verify'
}

time.sleep(2)
browser.get('http://www.nhc.gov.cn/xcs/yqfkdt/202203/1c35f7d0b9e248cc94b933925c48612c.shtml')
browser.add_cookie(cookie_dict=cookies)
time.sleep(3)
print(browser.find_elements(By.CLASS_NAME,"con")[0].text.replace("\n",""))
time.sleep(2)
browser.quit()