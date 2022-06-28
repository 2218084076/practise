import os
import random
import time

while True:

    for j in range(0, 2):
        for i in range(0, 10):
            x = random.randint(222, 250)
            y = random.randint(404, 440)
            # time.sleep(0.3)

            os.system('adb -s 869e65410721 shell input swipe %s %s %s %s 100' % (x, y, x, y))

            print("tap")
        time.sleep(1)

    time.sleep(5)
