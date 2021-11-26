import os
import time
import random
# os.system("adb -s a0e6c353 shell monkey -p com.ss.android.ugc.aweme.lite -c android.intent.category.LAUNCHER 1")
time.sleep(8)
n=1
while True:
	x=random.randint(498,598)
	a=random.randint(15,35)
	os.system(f"adb -s a0e6c353 shell input swipe {x} 2050 {x} 321 150")
	time.sleep(a)
	print(f"n={n},t={a}")
	n=n+1