import time

import pyautogui

while True:
    x, y = pyautogui.position()
    print('x=%s,y=%s' % (x, y))
    time.sleep(0.8)
