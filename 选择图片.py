import os
import time
print("选择图片")
img_add_num = 6
x_base = 320
x_add = 350
y_base = 443
y_add = 350
for i in range(0,img_add_num):
    x = x_base + x_add*(i%3)
    y = y_base + y_add*(int(i/3))
    os.system("adb shell input tap %s %s"%(x,y))
    time.sleep(2)