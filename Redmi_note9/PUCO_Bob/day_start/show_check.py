from PIL import Image, ImageGrab
import mss
import mss.tools
import time
import cv2 as cv
import pyautogui


import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib
from setting import android_x0
from setting import android_y0
from setting import android_x1
from setting import android_y1

model = tf.keras.models.load_model('models/my_model')
batch_size = 32
img_width = android_x1 - android_x0
img_height = android_y1 - android_y0

def get_android_img():
    starttime = time.time()
    with mss.mss() as sct:
        region = {
            "top":android_y0,
            "left":android_x0,
            "width":android_x1 - android_x0,
            "height":android_y1 - android_y0,
        }
        img = sct.grab(region)

        path_temp = "./hotpoor_autoclick_cache/record_temp.png"
        mss.tools.to_png(img.rgb,img.size,output=path_temp)
        endtime = time.time()
    return path_temp
def get_check_result(img_now):
    path_temp = "./hotpoor_autoclick_cache/record_temp.png"
    sunflower_path = pathlib.Path(path_temp)

    img = keras.preprocessing.image.load_img(
        sunflower_path, target_size=(img_height, img_width)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    
    # class_names = ['black', 'close', 'desktop', 'home', 'list', 'news', 'search', 'shop', 'video']
    class_names = ['black', 'close', 'desktop', 'home', 'list', 'news', 'search', 'share', 'shop', 'video']
    k = "None"
    if 100 * np.max(score)>=70:
        k = class_names[np.argmax(score)]
        print("当前页面为:",class_names[np.argmax(score)],100 * np.max(score))
    else:
        k = class_names[np.argmax(score)]
        print("80分以下当前页面为:",class_names[np.argmax(score)],100 * np.max(score))

    result = k
    actions = ["news","video","shop","list","share"]
    if result not in actions:
        result = "no action"
    return result
is_debug = True

is_debug = False

is_doing = False
is_left = True
action_now = "None"
# rem open xhs

if not is_debug:
    os.system("adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
    os.system("sleep 4")
    os.system("adb shell input tap 1000 150")
    os.system("sleep 2")
    os.system("adb shell input text PUCO")
    os.system("sleep 2")
    os.system("adb shell input tap 1000 150")
    os.system("sleep 3")
    os.system("adb shell input tap 380 360")
    os.system("sleep 3")
is_browser_count_max = 5
is_browser_count = 0

action_count = 0
action_count_num = 100
step_check_times = 5
if not is_debug:
    for i in range(0,action_count_num):
        print("action_count_num:%s/%s"%(i,action_count_num))
        action_now = "None"
        for step in ["list","card"]:
            step_check_times_now = 0
            while step_check_times_now<step_check_times:
                step_check_times_now +=1
                base_img = cv.imread(get_android_img(),0)
                action_now = get_check_result(base_img)
                cv.imshow("img",base_img)
                key = cv.waitKey(1)
                if key == ord("q"):
                    break
            print("当前页面为:",action_now)
            if step in ["list"]:
                if action_now in ["list"]:
                    if is_left:
                        os.system("adb shell input swipe 340 1200 340 400 1000")
                        if i > 3:
                            os.system("adb shell input swipe 340 600 340 1800 1000")
                            os.system("sleep 1")
                            os.system("adb shell input swipe 340 1400 340 200 1000")
                            os.system("sleep 2")
                        else:
                            os.system("adb shell input swipe 340 600 340 1200 1000")
                            os.system("sleep 1")
                            os.system("adb shell input swipe 340 1200 340 600 1000")
                            os.system("sleep 2")
                        os.system("adb shell input tap 340 500")
                        is_left = False
                    else:
                        os.system("adb shell input tap 800 500")
                        is_left = True
                    os.system("sleep 2")
            elif step in ["card"]:
                if action_now in ["shop","list"]:
                    os.system("adb shell input swipe 340 600 340 800 500")
                    os.system("sleep 1")
                    os.system("adb shell input tap 55 150")
                    os.system("sleep 1")
                elif action_now in ["news","video"]:
                    os.system("adb shell input tap 1000 155")
                    os.system("sleep 1")
                    #添加判断是否有分享页面
                    is_share_base_img = cv.imread(get_android_img(),0)
                    is_share_action_now = get_check_result(is_share_base_img)
                    cv.imshow("img",is_share_base_img)
                    key = cv.waitKey(1)
                    if key == ord("q"):
                        break
                    if is_share_action_now in ["share"]:
                        if action_now in ["news"]:
                            os.system("adb shell input tap 380 1876")
                        elif action_now in ["video"]:
                            os.system("adb shell input tap 523 1876")
                        os.system("sleep 2")
                        os.system("adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")
                        if is_browser_count == 0:
                            is_browser_count += 1
                            os.system("adb shell input tap 970 146")
                            os.system("sleep 4")
                        elif is_browser_count > is_browser_count_max:
                            is_browser_count = 0
                            os.system("adb shell input tap 970 146")
                            os.system("sleep 4")
                        else:
                            is_browser_count += 1
                            os.system("sleep 2")
                        # os.system("adb shell input swipe 330 780 330 780 1000")
                        if action_now in ["news"]:
                            os.system("adb shell input tap 330 780")
                        elif action_now in ["video"]:
                            os.system("adb shell input tap 760 780")
                        os.system("sleep 2")
                        os.system("adb shell input tap 398 1520")
                        os.system("sleep 2")
                        os.system("adb shell input tap 680 400")
                        os.system("sleep 1")
                        if action_now in ["news"]:
                            # os.system("adb shell input swipe 180 940 180 940 200")
                            os.system("adb shell input tap 180 940")
                            print("点击图文提交")
                        elif action_now in ["video"]:
                            # os.system("adb shell input swipe 850 940 850 940 200")
                            os.system("adb shell input tap 850 940")
                            print("点击视频提交") 
                        os.system("sleep 3")
                        os.system("adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
                        os.system("adb shell input tap 55 150")
                    else:
                        os.system("adb shell input tap 55 150")
                        os.system("sleep 1")
else:
    while True:
        base_img = cv.imread(get_android_img(),0)
        action_now = get_check_result(base_img)
        print(action_now)
        cv.imshow("img",base_img)
        key = cv.waitKey(1)
        if key == ord("q"):
            break

cv.destroyAllWindows()