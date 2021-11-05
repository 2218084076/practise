from selenium import webdriver
import time

'''d = webdriver.Chrome()
def get_Tiktok_url(u):
    u='http'+u.split('http')[1].split('复制')[0]
    d.get(u)
    time.sleep(20)
    for i in range(1,20):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        d.execute_script(js)
        time.sleep(2)
while True:
    get_Tiktok_url(input('抖音分享地址'))
    a = d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div[3]')
    b=a.find_element_by_class_name('_314bde61933468933fabb30f1507cdb2-scss').click()'''

#_9b365a9d76cfb9db759d93e586f25133-scss
#_9b365a9d76cfb9db759d93e586f25133-scss
d = webdriver.Chrome()
d.get('https://v.douyin.com/RBHmHQM/')
time.sleep(20)
n=0
n=int(n)
a=d.find_elements_by_class_name('_96ab12486b27de1f4a4a52e10dcb631a-scss')
for i in a:
    print(i[n].text)
    n=n+1
d.quit()