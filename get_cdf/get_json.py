"""
读取本地json文件
整理到excel中
"""
import json
import time

import xlwt

filename = '资生堂'
date_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
table = excel.add_sheet(time.strftime('%Y-%m-%d', time.localtime()), cell_overwrite_ok=True)

table.write(0, 0, "序号")
table.write(0, 1, "品牌")
table.write(0, 2, "商品名称")
table.write(0, 3, "商品编码")
table.write(0, 4, "商品价格")
table.write(0, 5, "商品促销")
table.write(0, 6, "规格")
table.write(0, 7, "商品详情数据")

'''urls = [
    ["1", "https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id="],

]
base_i = 1
for url in urls:

    a = requests.get(url[1])
    a = a.text
    b = json.loads(a)
    l = []

    for comment in b["comments"]:
        try:
            a_json = json.loads(comment[4])
        except:
            print("error:", url[0], comment[0])
            continue
        l.append(a_json)

    for i in range(0, len(l)):
        table.write(base_i + i, 0, i)
        table.write(base_i + i, 1, l[i]["detail-box-title"])
        table.write(base_i + i, 2, l[i]["product-name"])
        product_code_value = l[i]["product-code-value"]
        if product_code_value in "商品编号：":
            product_code_value = product_code_value.split("：")[1]
        print(product_code_value)
        table.write(base_i + i, 3, product_code_value)
        table.write(base_i + i, 4, l[i]["price-now"])
        table.write(base_i + i, 5, l[i]["promotion-item"])
        m = str(l[i]["property-item"].get("规格", ""))
        if m == "":
            m = str(l[i]["property-item"].get("规格：", ""))
        table.write(base_i + i, 6, m)
        table.write(base_i + i, 7, str(l[i]["property-item"]))

        print(base_i + i, l[i]["detail-box-title"], m)
        excel.save("cdf_220427.xls")
    base_i = base_i + len(l)'''
n = 1
with open('D:/cdf.json', 'r', encoding='utf-8') as f:
    infos_json = json.loads(f.read())
    print(infos_json)
    for i in infos_json:
        print(n, i)
        table.write(n, 0, n)
        table.write(n, 1, i.get('detail-box-title'))
        table.write(n, 2, i.get("product-name"))
        table.write(n, 3, i.get('product-code-value'))
        table.write(n, 4, i.get("price-now"))
        table.write(n, 5, i.get("promotion-item"))
        try:
            m = json.loads(i.get("property-item")).get("规格", "")
            m = m + json.loads(i.get("property-item")).get("保质期", "")
        except:
            m = i.get("property-item").get("规格", "")
        table.write(n, 6, m)
        try:
            table.write(n, 7, i.get('property-item'))
        except:
            table.write(n, 7, json.dumps(i.get('property-item'), ensure_ascii=False))
        excel.save("D:/Desktop/cdf_%s_%s.xls" % (filename, time.strftime('%Y-%m-%d', time.localtime())))
        n += 1
