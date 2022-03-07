import os
import time
import random
i=1
l=['869e65410721']
while i<150:
	for n in l:
		x1 = random.randint(86,482)
		y1 = random.randint(1172,1629)
		x2 = random.randint(622,1015)
		y2 = random.randint(1098,1620)
		# t=random.randint(2,5)
		os.system(f"adb -s {n} shell input tap {x1} {y1}")
		os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
		os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
		os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
		time.sleep(2)
		os.system(f"adb -s {n} shell input tap 71 120")
		os.system(f"adb -s {n} shell input tap {x2} {y2}")
		time.sleep(2)
		os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
		os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
		os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
		os.system(f"adb -s {n} shell input tap 71 120")
		time.sleep(1)
	print(f'n={i}\t')
	i += 1
print("End")
#adb devices查看连接设备
#869e65410721 Daniel
#a022d1760821 frank
#a0e6c353 realem Terry