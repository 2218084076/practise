import os
import time
import random
while True:
    t = random.randint(0,5)
    x = random.randint(135, 763)
    y = random.randint(525, 1337)
    for i in range(30):
        os.system('adb -s 9038c19f shell input tap %s %s && adb -s 9038c19f shell input tap %s %s'%(x,y,x,y))
        # os.system('adb -s 869e65410721 shell input tap %s %s && adb -s 869e65410721 shell input tap %s %s'%(x,y,x,y))

        print(i,t)
    time.sleep(t)

