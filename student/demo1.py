import reas
import json

url = 'http://www.cdfgsanya.com/product-list.html?sw=%E7%A7%91%E9%A2%9C%E6%B0%8F'
headers ={
	"origin": "www.cdfgsanya.com",
	"Referer": "http://www.cdfgsanya.com/product-list.html?sw=%E7%A7%91%E9%A2%9C%E6%B0%8F",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
response = requests.get(url,headers=headers)
requests.encoding='utf-8'
print(json.loads(requests))
