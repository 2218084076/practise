import os
import time
import random
i=1
l=['869e65410721','a0e6c353']
while i<280:
	# t=random.randint(3,8)
	# os.system("adb shell input tap 284 1328")
	# os.system("adb shell input swipe 951 994 80 975 100")
	# os.system("adb shell input swipe 951 994 80 975 100")
	# time.sleep(2)
	# os.system("adb shell input tap 71 120")
	# time.sleep(2)
	# os.system("adb shell input tap 800 1414")
	# # os.system("adb shell input swipe 951 994 80 975 100")
	# # os.system("adb shell input swipe 951 994 80 975 100")
	# time.sleep(t)
	# os.system("adb shell input tap 71 120")
	# time.sleep(1)
	for n in l:
		t=random.randint(3,8)
		os.system(f"adb -s {n} shell input tap 284 1328")
		os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
		os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
		time.sleep(2)
		os.system(f"adb -s {n} shell input tap 71 120")
		time.sleep(2)
		os.system(f"adb -s {n} shell input tap 800 1414")
		os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
		os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
		time.sleep(t)
		os.system(f"adb -s {n} shell input tap 71 120")
		time.sleep(1)
	print(f'n={i}',t,'s')
	i += 1
print("End")
#adb devices查看连接设备
#869e65410721 Daniel
#a022d1760821 frank
#a0e6c353 realem Terry