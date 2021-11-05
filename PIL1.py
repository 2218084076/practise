from PIL import Image


icon = r'D:\github\practise\1.png'
i = r'D:\github\practise\2.png'
i0 = Image.open(r'D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\img\xhs_head_cover_logo.png')
i1 = Image.open(icon)
i2 = Image.open(i)

layer = Image.new('RGBA',(600,800))
r,g,b,a = i1.split()
r1,g1,b1,a1 = i0.split()
i2.convert('RGBA')
layer.paste(i2,(0,0))

i1.convert('RGBA')
layer.paste(i1,(70,40), mask= a)

i0.convert('RGBA')
layer.paste(i0,(400,750))
layer.show()