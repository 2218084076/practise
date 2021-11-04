from PIL import Image

import numpy as np
from PIL import Image, ImageDraw

# Open the input image as numpy array, convert to RGB
img = Image.open(r"D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\60e87ea1000000002103b0ef_2.jpg").convert("RGB")
npImage = np.array(img)
h, w = img.size
# Create same size alpha layer with circle
alpha = Image.new('L', img.size, 0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0, 0, h, w], 0, 360, fill=255)
# Convert alpha Image to numpy array
npAlpha = np.array(alpha)
# Add alpha layer to RGB
npImage = np.dstack((npImage, npAlpha))
# Save with alpha
i = Image.fromarray(npImage)
# 修改像素
i.thumbnail(size=(100, 100), resample=Image.ANTIALIAS)
i.save(r'D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\2.png')


# i = r'D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\logo.png'
# icon = r''
# i1 = Image.open(icon)
# i2 = Image.open(i)
# layer = Image.new('RGBA', (600,800), (0, 0, 0, 0))
# r,g,b,a = i1.split()
# i2.convert('RGBA')
# layer.paste(i2,(0,0))
# i1.convert('RGBA')
# layer.paste(i1,(70,630), mask= a)
# layer.show()

