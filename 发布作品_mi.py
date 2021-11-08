import os
import time
print("开启web server\n")
# os.system("python D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\web.py")

#点击分享
os.system("adb shell input tap 1005 150")
time.sleep(2)
os.system("adb shell input tap 514 1860")
print("#打开浏览器\n")
os.system("adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")
time.sleep(6)
os.system("adb shell input tap 338 313")
os.system('adb shell input text "10.20.30.14:8888/demo/article"')
os.system("adb shell input tap 931 146")
time.sleep(60)
os.system("adb shell input tap 155 685")
time.sleep(3)
os.system("adb shell input swipe 155 685 155 685 500")
time.sleep(2)
os.system("adb shell input tap 123 564")
time.sleep(2)
os.system("adb shell input tap 283 788")
time.sleep(2)
os.system("adb shell input swipe 260 365 260 365 500")
time.sleep(3)
os.system("adb shell input tap 487 207")

print('点击小红书发布加号')
os.system('adb shell input tap 540 2137')
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
os.system('adb shell input tap 935 2144')
time.sleep(2)
os.system("")
# os.system("adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")