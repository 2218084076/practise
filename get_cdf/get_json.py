import requests
import json
import xlwt
import time
# https://www.qianshanghua.com/home/page/edit/7bd201e476e94bc4a1c3d5529083d8f7
# 2月份商品爬取
date_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('date_time',cell_overwrite_ok=True)

table.write(0,0,"序号")
table.write(0,1,"品牌")
table.write(0,2,"商品名称")
table.write(0,3,"商品编码")
table.write(0,4,"商品价格")
table.write(0,5,"商品促销")
table.write(0,6,"规格")
table.write(0,7,"商品详情数据")


urls=[
    ["1","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id="],
    ["2","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=c4f6a6c9bba8456886f66741b99f3adb"],
    ["3","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=5d3576892ce44d269bae3a8cbf739879"],
    ["4","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=69d24893560e477f91b64b5df0060af8"],
    ["5","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=28c67b6804fb4acc87b4a8077ddfb5c7"],
    ["6","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=727a1a8f76144fc59c049dc8f5458d2b"],
    ["7","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=f580b6f6d46347a8b3657dac94fbd47c"],
    ["8","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=501292f122174e42aacb249ca3099b0a"],
    ["9","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=e8fdbadbee5f42aa80fc56b17b2e4e28"],
    ["10","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=57af7ac19cb441d48526a8a36a9a5cb1"],
    ["11","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=ee1ffb206c764c8fb2590d39a71370e9"],
    ["12","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=58d5ad1d4d7642e2b540416b87e1ef78"],
    ["13","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=e8794ea239df4d63ad6629177cf8b75a"],
    ["14","https://www.qianshanghua.com/api/page/comment/load?chat_id=3f5a6f146e4e4763a18c0b5fc8f81609&comment_id=717cf92529c44318afcd815ffef7c86f"]

]
base_i=1
for url in urls:

    a = requests.get(url[1])
    a = a.text
    b = json.loads(a)
    l=[]

    for comment in b["comments"]:
        try:
            a_json = json.loads(comment[4])
        except:
            print("error:",url[0],comment[0])
            continue
        l.append(a_json)

    for i in range(0,len(l)):
        table.write(base_i+i,0,i)
        table.write(base_i+i,1,l[i]["detail-box-title"])
        table.write(base_i+i,2,l[i]["product-name"])
        product_code_value = l[i]["product-code-value"]
        if product_code_value in "商品编号：":
            product_code_value = product_code_value.split("：")[1]
        print(product_code_value)
        table.write(base_i+i,3,product_code_value)
        table.write(base_i+i,4,l[i]["price-now"])
        table.write(base_i+i,5,l[i]["promotion-item"])
        m = str(l[i]["property-item"].get("规格", ""))
        if m == "":
            m=str(l[i]["property-item"].get("规格：",""))
        table.write(base_i+i,6,m)
        table.write(base_i+i,7,str(l[i]["property-item"]))
        
        print(base_i+i,l[i]["detail-box-title"],m)
        excel.save("cdf_220427.xls")
    base_i=base_i+len(l)


