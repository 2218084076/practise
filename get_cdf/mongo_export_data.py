#
"""export data"""
import json
import time
from pathlib import Path

import pymongo
import xlwt

data_list = ['']
index_dic = {
    "商品编码": "$商品编码",
    "link": "$link"}

filename = '补充'
mongo_uri = 'localhost:27017'
mongo_db = 'cdf'
table_name = '20220826补充'

date_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
excel = xlwt.Workbook(encoding='utf-8')
table = excel.add_sheet('cdf')

table.write(0, 0, "序号")
table.write(0, 1, "品牌")
table.write(0, 2, "商品名称")
table.write(0, 3, "商品编码")
table.write(0, 4, "商品价格")
table.write(0, 5, "商品促销")
table.write(0, 6, "规格")
table.write(0, 7, "商品详情数据")

client = pymongo.MongoClient(mongo_uri)
my_db = client[mongo_db]
col = my_db[table_name]

col.distinct('商品编码')

documents = col.find()
n = 1

for i in list(documents):
    print(n, i)
    table.write(n, 0, n)
    table.write(n, 1, i.get('品牌'))
    table.write(n, 2, i.get("商品名称"))

    table.write(n, 3, i.get('商品编码'))
    table.write(n, 4, i.get("当前价格"))
    table.write(n, 5, i.get("商品促销"))
    table.write(n, 8, i.get('link'))
    try:
        m = i.get("详细信息").get("规格", "")
        m = m + i.get("详细信息").get("规格：", "")
    except Exception as e:
        print("error", e)
        m = i.get("详细信息").get("规格：", "")
    table.write(n, 6, m)
    try:
        table.write(n, 7, json.dumps(i.get('详细信息'), ensure_ascii=False))
    except Exception as e:
        print("error", e)
        table.write(n, 7, json.dumps(i.get('详细信息')), ensure_ascii=False)
    excel.save(Path("D:/Desktop/%s_%s.xls" % (filename, time.strftime('%Y%m%d%H', time.localtime()))))
    n += 1
