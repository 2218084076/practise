#!/bin/env python
# -*- coding: utf-8 -*-
import json

import requests
import xlwt

excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
table = excel.add_sheet('1', cell_overwrite_ok=True)
table.write(0, 0, "")
table.write(0, 1, "品牌")
table.write(0, 2, "商品名称")
table.write(0, 3, "商品编码")
table.write(0, 4, "商品价格")
table.write(0, 5, "商品促销")
table.write(0, 6, "规格")
table.write(0, 7, "商品详情数据")

urls = [
    ["博主信息", "https://www.qianshanghua.com/api/page/comment/load?chat_id=502c0d441b2a42b6a145a367bc6d1125&comment_id="]
]
base_i = 1
for url in urls:
    a = requests.get(url[1])
    a = a.text
    b = json.loads(a)
    l1 = []
    for comment in b["comments"]:
        try:
            a_json = json.loads(comment[4])
        except Exception as e:
            print("error:", url[0], comment[0], e)
            continue
        l.append(a_json)
    for i in range(0, len(l)):
        table.write(base_i + i, 0, i)
        table.write(base_i + i, 1, l1[i].get("name", "no name"))
        table.write(base_i + i, 2, l1[i].get("fan", "no fan"))
        table.write(base_i + i, 3, l1[i].get("shop", "no shop"))
        table.write(base_i + i, 4, l1[i].get("wechat", "no wechat"))
        table.write(base_i + i, 5, l1[i].get("phone", "no phone"))
        table.write(base_i + i, 6, l1[i].get("introduce", "no introduce"))
        table.write(base_i + i, 7, l1[i].get("dou_id", "no id"))

        print(i, l[i]["name"])
    excel.save("dou.xls")
