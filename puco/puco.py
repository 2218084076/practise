import os
import random
import time
while True:

    for j in range(0,2):
        for i in range(0,10):
            x = random.randint(222, 250)
            y = random.randint(404,440)
            # time.sleep(0.3)
            # os.system(f'adb -s 869e65410721 shell input tap %s %s'%(x,y))
            os.system('adb -s 869e65410721 shell input swipe %s %s %s %s 100'%(x,y,x,y))

            print("tap")
        time.sleep(1)
    # os.system(f'adb -s 869e65410721 shell input tap 222 565')
    # os.system(f'adb -s 869e65410721 shell input tap 222 565')
    # os.system(f'adb -s 869e65410721 shell input tap 222 565')
    # os.system(f'adb -s 869e65410721 shell input tap 222 565')
    # os.system(f'adb -s 869e65410721 shell input tap 222 565')


    time.sleep(5)

    # os.system(f'adb -s 869e65410721 shell input swipe {x} {y} {x} {y} 10')

# os.system('adb -s 869e65410721 shell "while true;do input tap 222 565 & input tap 222 565 & sleep 0.3;done"')

