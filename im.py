import numpy as np
from PIL import Image, ImageDraw

# Open the input image as numpy array, convert to RGB
img = Image.open("/Users/ryan/PycharmProjects/web2.0/local_web/static/icon/icon.jpg").convert("RGB")
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
i.save('/Users/ryan/PycharmProjects/web2.0/local_web/static/icon/icon.png')