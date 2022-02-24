import requests
import json
import xlwt

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)
table.write(0,0,"序号")
table.write(0,1,"日期")
table.write(0,2,"博主名字")
table.write(0,3,"开播时间")
table.write(0,4,"直播间成交金额")
table.write(0,5,"观看人次")
table.write(0,6,"千次观看成交金额")


urls=[
    ["1","https://www.qianshanghua.com/api/page/comment/load?chat_id=6a5d11bb4b8a458985dac21079802937&comment_id="],
    ["2","https://www.qianshanghua.com/api/page/comment/load?chat_id=6a5d11bb4b8a458985dac21079802937&comment_id=5d47f70c75fe4db98cf11d74b02471af"],
    ["3","https://www.qianshanghua.com/api/page/comment/load?chat_id=6a5d11bb4b8a458985dac21079802937&comment_id=b9822560b8e3491b91abe36fada85283"],
    ["4","https://www.qianshanghua.com/api/page/comment/load?chat_id=6a5d11bb4b8a458985dac21079802937&comment_id=97f82440b76c4027b71426875db67788"],
    ["5","https://www.qianshanghua.com/api/page/comment/load?chat_id=6a5d11bb4b8a458985dac21079802937&comment_id=ce7102a5ec804425b3d10ea00102b022"],
    ["6","https://www.qianshanghua.com/api/page/comment/load?chat_id=6a5d11bb4b8a458985dac21079802937&comment_id=2bbdc46177164ac182f7ce06a9edb8d5"],
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
        table.write(base_i+i,1,l[i]["date"])

        table.write(base_i+i,2,l[i]["name"])
        table.write(base_i+i,3,l[i]["time"])
        table.write(base_i+i,4,l[i]["clinch"])
        table.write(base_i+i,5,l[i]["number"])
        table.write(base_i + i, 6,l[i]["thousands"])
        excel.save(r"D:\github\practise\dou_\dou_220223.xls")
        print(i,l[i]["name"])
    base_i=base_i+len(l)


