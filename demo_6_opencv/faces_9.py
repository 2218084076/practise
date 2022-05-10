import cv2
import dlib
import time
import glob
import numpy as np


import os
import time
pic_file = os.listdir(r"D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\pic1")
pic_list = os.listdir(r"D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\test")

l = []

for i in pic_list:
    for n in pic_file:
        j = i.split('_')[0]
        if j == n.split('_')[0] and n.split('_')[1]!='YSL':
            path = "D:/github/1/hotpoor_autoclick_xhs/demo_6_opencv/test/"+i
            l.append(path)
            # print(path)
# print(l)

for n in range(0,len(l),9):
    l1 = l[n:n+9]
    print(l1)
    imgs, heights, widths = [], [], []
    # read imgs
    for f in l1:
        img = cv2.imread(f, -1)  # 参数-1表示返回原图
        h, w = img.shape[:2]  # 切片
        heights.append(h)
        widths.append(w)
        imgs.append(img)
    # set minimum heights and weights
    min_height = min(heights)
    min_width = min(widths)
    # resize imgs
    name = l1[0].split('/test/')[1].split('_')[0]
    print(name)
    for i, x in enumerate(imgs):
        # i为每个图像的序号, x为每个图像的多维像素矩阵
        imgs[i] = x[:min_height:4, :min_width:4]  # 切片 以步长为3
    # concatenation
    img0 = np.concatenate(imgs[:3], 1)  # 横着拼三个
    img1 = np.concatenate(imgs[3:6], 1)  # 横着拼三个
    img2 = np.concatenate(imgs[6:], 1)  # 横着拼三个
    # resize logo
    imgLogo = cv2.imread(r"D:\Terry\p\LOGO\puco.jpg", cv2.IMREAD_UNCHANGED)
    h, w = img0.shape[:2]
    dim = (w, int(h / 2))
    print(dim)
    imgLogo = cv2.resize(imgLogo, dim, interpolation=cv2.INTER_AREA)
    # cv2.imshow('logo', imgLogo)
    img9 = np.concatenate([img0, img1, img2, imgLogo], 0)  # 竖着拼起来
    h,w = img9.shape[:2]

    # resize final pic
    print(min_width, min_height)
    # img9 = cv2.resize(img9, (1080, 1439), interpolation=cv2.INTER_AREA)
    cv2.imwrite(f"D:/Terry/p/faces/{name}_PUCO.jpg", img9)
    # cv2.imshow('0',img0)
    # cv2.imshow('1',img1)
    # cv2.imshow('2',img2)
    # cv2.imshow('logo',imgLogo)
    # cv2.imshow('9',img9)
    cv2.waitKey(0)
print('End')
