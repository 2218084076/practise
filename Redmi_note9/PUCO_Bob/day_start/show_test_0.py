import os
import time
# os.system("adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
# os.system("sleep 4")
# os.system("adb shell input tap 1000 150")
# os.system("sleep 2")
# os.system("adb shell input text PUCO")
# os.system("sleep 2")
# os.system("adb shell input tap 1000 150")

# os.system("adb shell input swipe 340 800 340 500 1000")

for i in range(0,50):
    os.system("adb shell input swipe 340 1200 340 400 1000")
    os.system("adb shell input swipe 340 600 340 1800 1000")
    time.sleep(1)
    os.system("adb shell input swipe 340 1400 340 200 1000")
    time.sleep(2)
