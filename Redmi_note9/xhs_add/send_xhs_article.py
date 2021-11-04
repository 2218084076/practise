# 直接回填
import pyautogui
import os
import time

print("打开小红书")
os.system("adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
time.sleep(5)
print("点击新建图文")
os.system("adb shell input tap 547 2140")
time.sleep(2)

print("选择图片")
img_add_num = 7
x_base = 307
x_add = 365
y_base = 413
y_add = 365
for i in range(0,img_add_num):
    x = x_base + x_add*(i%3)
    y = y_base + y_add*(int(i/3))
    os.system("adb shell input tap %s %s"%(x,y))
    time.sleep(0)

print("选择下一步")
os.system("adb shell input tap 958 2170")
time.sleep(2)

print("选择下一步")
os.system("adb shell input tap 1000 160")
time.sleep(2)

print("打开浏览器")
os.system("adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")
time.sleep(5)
os.system("adb shell input tap 455 496")
os.system("adb shell input swipe 455 496 455 496 1000")
time.sleep(1)
os.system("adb shell input tap 406 700")
time.sleep(1)
os.system("adb shell input tap 484 331")

print("选择title")
os.system("adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
time.sleep(2)
os.system("adb shell input swipe 600 625 600 625 1000")
# 粘贴
os.system("adb shell input tap 100 465")
time.sleep(2)

print("打开浏览器")
os.system("adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")
time.sleep(5)
os.system("adb shell input tap 555 555")
os.system("adb shell input swipe 555 555 555 555 1000")
time.sleep(1)
os.system("adb shell input tap 435 425")
time.sleep(1)
os.system("adb shell input tap 490 400")

print("选择正文")
os.system("adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
time.sleep(2)
os.system("adb shell input swipe 600 825 600 825 1000")
# 粘贴
os.system("adb shell input tap 100 588")
time.sleep(2)

print("发布笔记")
os.system("adb shell input tap 738 2130")

