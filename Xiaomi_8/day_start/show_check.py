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

model = tf.keras.models.load_model('models/my_model')
batch_size = 32
img_width = 450
img_height = 944


android_x0 = 734
android_y0 = 68
android_x1 = 1184
android_y1 = 1012
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
    
    class_names=['home', 'list', 'news', 'search', 'video']
    k = "None"
    if 100 * np.max(score)>=90:
        k = class_names[np.argmax(score)]
        print("当前页面为:",class_names[np.argmax(score)],100 * np.max(score))
    result = k
    actions = ["news","video"]
    if result not in actions:
        result = "no action"
    return result
while True:
    base_img = cv.imread(get_android_img(),0)
    # gray_img = cv.cvtColor(base_img, cv.COLOR_BGR2GRAY)
    get_check_result(base_img)
    cv.imshow("img",base_img)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
cv.destroyAllWindows()