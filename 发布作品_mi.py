import os
import time
from tool_article import get_article_info
print("开启web server\n")
# os.system("python D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\web.py")


os.system("adb shell input tap 1005 150")
time.sleep(2)
os.system("adb shell input tap 514 1860")
print("#打开浏览器\n")
os.system("adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")
time.sleep(6)
os.system("adb shell input tap 338 313")
os.system('adb shell input text "192.168.11.7:8888/demo/article"')
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

# os.system("adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")