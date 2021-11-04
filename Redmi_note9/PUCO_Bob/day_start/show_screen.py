import os
import cv2
import time

path = "C:/Users/lenovo/Documents/Sites/github/hotpoor_autoclick_xhs/Xiaomi_8/day_start/hotpoor_autoclick_cache"
cache = "hotpoor_autoclick_cache/screen.png"
def get_image():
    os.system(f"adb shell screencap -p /sdcard/%s"%cache)
    os.system(r"adb pull /sdcard/%s %s"%(cache,path))
def load_image():
    i1 = cv2.imread("%s/screen.png"%path)
    scale_percent=50
    w=int(i1.shape[1]*scale_percent/100)
    h=int(i1.shape[0]*scale_percent/100)
    dim=(w,h)
    resized = cv2.resize(i1,dim,interpolation=cv2.INTER_AREA)
    cv2.imshow("path", resized)
    k = cv2.waitKey(0)


while True:
    get_image()
    print("get_image")
    # load_image()
    i1 = cv2.imread("%s/screen.png"%path)
    scale_percent=40
    w=int(i1.shape[1]*scale_percent/100)
    h=int(i1.shape[0]*scale_percent/100)
    dim=(w,h)
    resized = cv2.resize(i1,dim,interpolation=cv2.INTER_AREA)
    cv2.imshow("path", resized)
    k = cv2.waitKey(1)