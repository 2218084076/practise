"""export data"""
import time

import pandas as pd
import pymongo
import xlwt

data_list = []

filename = 'cdf_'
date_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
excel = xlwt.Workbook(encoding='utf-8')
table = excel.add_sheet(' ')

table.write(0, 0, "序号")
table.write(0, 1, "品牌")
table.write(0, 2, "商品名称")
table.write(0, 3, "商品编码")
table.write(0, 4, "商品价格")
table.write(0, 5, "商品促销")
table.write(0, 6, "规格")
table.write(0, 7, "商品详情数据")

mongo_uri = 'localhost:27017'
mongo_db = 'cdf'
table_name = 'cdf_20220729补充'

client = pymongo.MongoClient(mongo_uri)
my_db = client[mongo_db]
table = my_db[table_name]
documents = table.find()

data = pd.DataFrame(list(documents))

data.to_excel('cdf_20220729补充.xls', encoding='utf-8')
print(data[['商品名称']])
# n = 1
#
# for i in list(documents):
#     print(n, i)
#     table.write(n, 0, n)
#     table.write(n, 1, i.get('detail-box-title'))
#     table.write(n, 2, i.get("product-name"))
#
#     table.write(n, 3, i.get('product-code-value'))
#     table.write(n, 4, i.get("price-now"))
#     table.write(n, 5, i.get("promotion-item"))
#     try:
#         m = json.loads(i.get("property-item")).get("规格", "")
#         m = m + json.loads(i.get("property-item")).get("保质期", "")
#     except Exception as e:
#         print("error", e)
#         m = i.get("property-item").get("规格", "")
#     table.write(n, 6, m)
#     try:
#         table.write(n, 7, i.get('property-item'))
#     except Exception as e:
#         print("error", e)
#         table.write(n, 7, json.dumps(i.get('property-item')))
#     excel.save("D:/Desktop/%s_%s.xls" % (filename, time.strftime('%Y-%m-%d', time.localtime())))
#     n += 1
