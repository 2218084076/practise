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

share = input('抖音分享地址：')
share='http'+share.split('http')[1].split('复制')[0]
d = webdriver.Chrome()
d.get(share)
time.sleep(20)

for n in range(1,101):
    d.execute_script('window.scrollBy(0,1000)')
    time.sleep(1)

a=d.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div[3]/div/div/div[4]').find_elements_by_class_name('aa8946e6a10e3788dca09663eb82fc99-scss')
#赞 _314bde61933468933fabb30f1507cdb2-scss fd385a3d6601897cdbce6252a3346600-scss
#名_52058b306f496907c5d55c0facb81886-scss
for i in range(0,len(a)+1):
    if a[i].find_element_by_class_name('_52058b306f496907c5d55c0facb81886-scss').text.split('2021')[0] == '努力的打工人':
        a[i].find_element_by_class_name('_314bde61933468933fabb30f1507cdb2-scss').click()
    else:
        print(a[i].find_element_by_class_name('_52058b306f496907c5d55c0facb81886-scss').text)


