from selenium import webdriver
import time
import xlwt
import datetime
excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)
now_time = datetime.datetime.now().strftime('%Y-%m-%d')
driver = webdriver.Chrome('C:/Users/LENOVO/anaconda3/Scripts/chromedriver.exe')
url = 'https://www.douyin.com/search/%E8%8B%8F%E5%B7%9E%E6%88%BF%E4%BA%A7?publish_time=0&sort_type=2&source=search_sug&type=video'
driver.get(url)
time.sleep(50)
for i in range(1,456):
    d1 = driver.find_element_by_xpath(
        f'//*[@id="root"]/div/div[2]/div/div[2]/div[2]/ul/li[{i}]/div/div/a')
    table.write(i,1,d1.text)
    # d1 博主名
    print(i,d1.text)
    d3 = driver.find_element_by_xpath(
        f'//*[@id="root"]/div/div[2]/div/div[2]/div[2]/ul/li[{i}]/div/a[2]')
    # 文案
    table.write(i,3,d3.text)
    urls_p = driver.find_elements_by_xpath(
        f'//*[@id="root"]/div/div[2]/div/div[2]/div[2]/ul/li[{i}]/div/a[1]')
    for u in urls_p:
        url_works = u.get_attribute("href")
        table.write(i,4,u.get_attribute("href"))
        print(url_works)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
        excel.save(f"D:/Desktop/苏州房产1-{now_time}.xls")
    excel.save(f"D:/Desktop/苏州房产1-{now_time}.xls")
    time.sleep(2)
driver.quit()

from selenium import webdriver
driver = webdriver.Chrome()