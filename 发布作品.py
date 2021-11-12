import os
import time
print('打开浏览器')
os.system('adb -s 869e65410721 shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1')
time.sleep(10)
print('')




print('#打开小红书')
os.system('adb -s 869e65410721 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1')

