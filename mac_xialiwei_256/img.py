import numpy as np
from PIL import Image, ImageDraw

# Open the input image as numpy array, convert to RGB
img = Image.open(r"D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\618263d9000000002103f6bb_2.jpg").convert("RGB")
npImage = np.array(img)
h, w = img.size
print('h,w =',h,w)
# Create same size alpha layer with circle
alpha = Image.new('L', img.size, 0)
print('alpha=',alpha)
draw = ImageDraw.Draw(alpha)
print('draw=',draw)
draw.pieslice([0, 0, h, w], 0, 360, fill=255)
# Convert alpha Image to numpy array
npAlpha = np.array(alpha)
# Add alpha layer to RGB
npImage = np.dstack((npImage, npAlpha))
# Save with alpha
i = Image.fromarray(npImage)
# 修改像素
i.thumbnail(size=(100, 100), resample=Image.ANTIALIAS)
i.save(r'D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\icon.png')


# ffmpeg -y -r 1 -i %d.jpg -vcodec libx264 t.mp4