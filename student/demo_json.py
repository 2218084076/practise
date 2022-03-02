import json
dics=[
	{
	"a":[1,2,3,4,5,6],
	# 列表类型
	"b":{"qqwe":"12343dasffg"},
	# 字典类型
	"c":"3",
	# 字符串类型
	"d":1234
	# int类型
	},
	{
	"a":[1,2,3,4,5,6],
	"b":{"qqwe":"12343dasffg"},
	"c":"3",
	"d":["q","d","f"]
	},
	{
	"a":[1,2,3,4,5,6],
	"b":{"qqwe":"12343dasffg"},
	"c":"3",
	"d":["q","d","f"]
	}]
with open ("record.json","w") as f:
	json.dump(dics,f)

with open("record.json",'r') as load_f:
	load_json = json.load(load_f)
	print(load_json)
