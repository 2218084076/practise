from selenium import webdriver
import time
import xlwt
import xlrd
import datetime
import random

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('小红书博主及文章信息',cell_overwrite_ok=True)
table.write(0,1,'name')
table.write(0,2,'title')
table.write(0,3,'content')
table.write(0,4,'item_id')
table.write(0,5,'article_url')
table.write(0,6,'user_url')

urls = ['7 碎碎念的岁岁发布了一篇小红书笔记，快来看吧！ 😆 KjnkMxzYCYLZkxC 😆 http://xhslink.com/CbPuLe，复制本条信息，打开【小红书】App查看精彩内容！',
        '76 哐哐-.发布了一篇小红书笔记，快来看吧！ 😆 fQ9p9HAiPZrwvsH 😆 http://xhslink.com/CJvBLe，复制本条信息，打开【小红书】App查看精彩内容！',
        '90 🍋柠萌￢ε￢发布了一篇小红书笔记，快来看吧！ 😆 OlvNhxAFScyQub1 😆 http://xhslink.com/bmpzLe，复制本条信息，打开【小红书】App查看精彩内容！',
        '58 弓长张可爱发布了一篇小红书笔记，快来看吧！ 😆 FU5q2lNL54b6Vv0 😆 http://xhslink.com/iMmuLe，复制本条信息，打开【小红书】App查看精彩内容！',
        '75 一两发布了一篇小红书笔记，快来看吧！ 😆 XvET9gIkZV2eEds 😆 http://xhslink.com/HCCpLe，复制本条信息，打开【小红书】App查看精彩内容！',
        ]

def get_note(url_list):
    n = 1
    urls = url_list
    for url in urls:
        driver = webdriver.Chrome()
        url = 'http'+url.split("http")[1].split(', 复制')[0]
        table.write(n,7,url)
        driver.get(url)
        driver.minimize_window()
        time.sleep(4)
        article_url = driver.current_url
        table.write(n,5,article_url)
        print(f'{n}\n作品链接：',article_url)
        item_id = article_url.split('/item/')[1].split('?xhsshare')[0]
        table.write(n,4,item_id)
        print('作品item_id',item_id)
        title = driver.find_element_by_class_name('note-top').text
        table.write(n,2,title)
        print('title：',title)
        content = driver.find_element_by_class_name('content').text
        table.write(n,3,content)
        print('文案：\n',content)
        name = driver.find_element_by_class_name('name').text
        table.write(n,1,name)
        print('博主名',name)
        driver.find_element_by_class_name("author-item").find_element_by_class_name("author-info").click()
        driver.minimize_window()

        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        user_url = driver.current_url
        table.write(n,6,user_url)
        print('博主链接：',user_url)
        user_id = user_url.split("/user/profile/")[1]
        print('user_id: ',user_id)
        excel.save(f"D:/Desktop/小红书.xls")
        n+=1
        driver.quit()
    print('End')

def excel(file):
    w = xlrd.open_workbook(file)
    sheet_name = w.sheet_names()
    s = w.sheet_by_name(sheet_name[0])
    name_list = s.col_values(1)[1:]
    return name_list

get_note(urls)
