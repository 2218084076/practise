import pyautogui
import time
while True:
    x,y = pyautogui.position()
    print('"x":%s,\n"y":%s,\n\n'%(x,y))
    time.sleep(0.1)
