import os
import time
import random
i=1
# l=['869e65410721']
while i<280:
	os.system("adb shell input tap 284 1328")
	os.system("adb shell input swipe 951 994 80 975 100")
	os.system("adb shell input swipe 951 994 80 975 100")
	time.sleep(2)
	os.system("adb shell input tap 71 120")
	time.sleep(2)
	os.system("adb shell input tap 800 1414")
	os.system("adb shell input swipe 951 994 80 975 100")
	os.system("adb shell input swipe 951 994 80 975 100")
	time.sleep(1)
	os.system("adb shell input tap 71 120")
	time.sleep(1)
	print(f'n={i}')
	i += 1

#adb devices查看连接设备
#869e65410721 Daniel
#a022d1760821 frank
#a0e6c353 realem Terry