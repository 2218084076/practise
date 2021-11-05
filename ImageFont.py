from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

target = r'D:\github\practise\mac_xialiwei_256\local_web\static\upload\60e87ea1000000002103b0ef_0.jpg'

img = Image.open(target)
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(r"C:\WINDOWS\Fonts\FZSTK.TTF", 40, encoding="unic")
#windows 路径可以直接设置 "simsun.ttc"
draw.text((100,200),'PUCO集美手账',(254,254,254),font=font)
img.show()