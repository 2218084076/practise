import pyautogui
import time
while True:
    time.sleep(0.3)
    x,y = pyautogui.position()
    print("\t")
    print('"x":%s,\n"y":%s,'%(x,y))