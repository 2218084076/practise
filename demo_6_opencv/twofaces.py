import cv2
import dlib
import time
import glob
import numpy as np


def x2faces(num):
    imgs, heights, widths = [], [], []
    # read imgs
    for f in glob.glob(r"D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\afterWork\*.jpg"):
        if 'YSL' in f:
            img = cv2.imread(f, -1)  # 参数-1表示返回原图
            h, w = img.shape[:2]  # 切片
            heights.append(h)
            widths.append(w)
            imgs.append(img)
    # set minimum heights and weights
    min_height = min(heights)
    min_width = min(widths)
    # resize imgs
    for i, x in enumerate(imgs):
        # i为每个图像的序号, x为每个图像的多维像素矩阵
        imgs[i] = x[:min_height:2, :min_width:2]  # 切片 以步长为3
    # concatenation
    img0 = np.concatenate(imgs[:2], 1)  # 横着拼三个
    # resize logo
    imgLogo = cv2.imread(r"D:\Terry\p\LOGO\YSL.jpg",cv2.IMREAD_UNCHANGED)
    h, w = img0.shape[:2]
    dim = (w, int(h/3))
    imgLogo = cv2.resize(imgLogo, dim, interpolation = cv2.INTER_AREA)
    img9 = np.concatenate([img0,imgLogo], 0)# 竖着拼起来
    #resize final pic
    print(min_width,min_height)
    #img9 = cv2.resize(img9,(1080,1439), interpolation = cv2.INTER_AREA)
    h,w = img9.shape[:2]
    if int(h*0.75) != w:
        print('not 4:3')
        x = int(w*1.25)-h
        img9 = cv2.copyMakeBorder(img9,int(x/2), int(x/2), 0, 0, cv2.BORDER_CONSTANT, value=(0,0,0))
    cv2.imwrite("final/1x1%s.jpg"% num, img9)
