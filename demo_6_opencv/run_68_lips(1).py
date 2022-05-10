# 1.该代码用于提取人脸68个关键点
# 2.并提取嘴部mask
# coding=utf-8
import os

import cv2
import dlib
import numpy as np
import time
from skimage import measure, data, color

# JAW_POINTS = list(range(0, 17))
# FACE_POINTS = list(range(17, 68))
# BROW_POINTS = list(range(17, 27))
# NOSE_POINTS = list(range(27, 36))
# EYE_POINTS = list(range(36, 48))
# MOUTH_POINTS = list(range(48, 61))

# camera = cv2.VideoCapture(0)
# camera = cv2.VideoCapture("./a.mp4")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./data/dlib/shape_predictor_68_face_landmarks.dat")
id_list = os.listdir("D:/github/1/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/files")
def beauty_face(img):
    '''
    Dest =(Src * (100 - Opacity) + (Src + 2 * GuassBlur(EPFFilter(Src) - Src + 128) - 256) * Opacity) /100 ;
    https://my.oschina.net/wujux/blog/1563461
    '''

    dst = np.zeros_like(img)
    # int value1 = 3, value2 = 1; 磨皮程度与细节程度的确定
    v1 = 3
    v2 = 1
    dx = v1 * 5  # 双边滤波参数之一
    fc = v1 * 12.5  # 双边滤波参数之一
    p = 0.1

    temp4 = np.zeros_like(img)

    temp1 = cv2.bilateralFilter(img, dx, fc, fc)
    temp2 = cv2.subtract(temp1, img)
    temp2 = cv2.add(temp2, (10, 10, 10, 128))
    temp3 = cv2.GaussianBlur(temp2, (2 * v2 - 1, 2 * v2 - 1), 0)
    temp4 = cv2.add(img, temp3)
    dst = cv2.addWeighted(img, p, temp4, 1 - p, 0.0)
    dst = cv2.add(dst, (10, 10, 10, 255))
    return dst

def beauty_face2(src):
    '''
    Dest =(Src * (100 - Opacity) + (Src + 2 * GuassBlur(EPFFilter(Src) - Src + 128) - 256) * Opacity) /100 ;
    '''

    dst = np.zeros_like(src)
    # int value1 = 3, value2 = 1; 磨皮程度与细节程度的确定
    v1 = 3
    v2 = 1
    dx = v1 * 5  # 双边滤波参数之一
    fc = v1 * 12.5  # 双边滤波参数之一
    p = 0.1

    temp4 = np.zeros_like(src)

    temp1 = cv2.bilateralFilter(src, dx, fc, fc)
    temp2 = cv2.subtract(temp1, src)
    temp2 = cv2.add(temp2, (10, 10, 10, 128))
    temp3 = cv2.GaussianBlur(temp2, (2 * v2 - 1, 2 * v2 - 1), 0)
    temp4 = cv2.subtract(cv2.add(cv2.add(temp3, temp3), src), (10, 10, 10, 255))

    dst = cv2.addWeighted(src, p, temp4, 1 - p, 0.0)
    dst = cv2.add(dst, (10, 10, 10, 255))
    return dst

def mask_add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """
    b_channel, g_channel, r_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道

    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))  # 融合通道

    # print(len(img_new),len(img_new[0]),img_new[0][0])
    h = len(img_new)
    w = len(img_new[0])
    for col in range(0, h):
        for row in range(0, w):
            [g, b, r, alpha] = img_new[col][row]
            if r == 0 and g == 0 and b == 0:
                img_new[col][row][3] = 0
            else:
                img_new[col][row][3] = int(255*0.4)
    return img_new

def add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """

    b_channel, g_channel, r_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道

    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))  # 融合通道
    return img_new

def del_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """

    b_channel, g_channel, r_channel, alpha_channel = cv2.split(img)  # 剥离jpg图像通道

    img_new = cv2.merge((b_channel, g_channel, r_channel))  # 融合通道
    return img_new

def merge_img(jpg_img, png_img, y1, y2, x1, x2):
    """ 将png透明图像与jpg图像叠加
        y1,y2,x1,x2为叠加位置坐标值
    """

    # 判断jpg图像是否已经为4通道
    if jpg_img.shape[2] == 3:
        jpg_img = add_alpha_channel(jpg_img)

    '''
    当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
    这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加
    '''
    yy1 = 0
    yy2 = png_img.shape[0]
    xx1 = 0
    xx2 = png_img.shape[1]

    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > jpg_img.shape[1]:
        xx2 = png_img.shape[1] - (x2 - jpg_img.shape[1])
        x2 = jpg_img.shape[1]
    if y2 > jpg_img.shape[0]:
        yy2 = png_img.shape[0] - (y2 - jpg_img.shape[0])
        y2 = jpg_img.shape[0]

    # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
    alpha_png = png_img[yy1:yy2, xx1:xx2, 3] / 255.0
    alpha_jpg = 1 - alpha_png

    # 开始叠加
    for c in range(0, 3):
        jpg_img[y1:y2, x1:x2, c] = ((alpha_jpg * jpg_img[y1:y2, x1:x2, c]) + (alpha_png * png_img[yy1:yy2, xx1:xx2, c]))

    return jpg_img

# is_true = True
# while is_true:
# ret, img = camera.read()
def coloring(imgfile):
    aim_list = ["MM01", "MM02", "MM03", "MM04", "MM05", "MM06", "MM07", "MM08"]
    for aim in aim_list:
        ret = True
        img = cv2.imread(imgfile)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if ret:
            dets = detector(gray, 0)
            h, w, c = img.shape
            print(h, w, c)
            # mask = np.zeros((img.shape), dtype=np.uint8)
            mask = np.zeros((img.shape), dtype=np.uint8)
            for face in dets:
                shape = predictor(img, face)  # 寻找人脸的68个标定点
                # 遍历所有点，打印出其坐标，并圈出来
                for idx, pt in enumerate(shape.parts()):
                    pt_pos = (pt.x, pt.y)
                    # cv2.circle(img, pt_pos, 2, (0, 255, 0), 1)
                    # font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
                    # cv2.putText(img,str(idx),pt_pos,font,0.4,(0,0,255),1,cv2.LINE_AA)

                # cv2.imshow("image", img)

                # h, w, c = img.shape
                # # 手工绘制ROI区域
                # mask = np.zeros((h, w), dtype=np.uint8)

                list_x = []
                list_y = []
                start_pt_48 = None
                start_pt_60 = None
                for idx, pt in enumerate(shape.parts()):
                    # if idx >= 48 and idx <= 59:
                    if idx >= 48 and idx <= 67:
                        list_x.append(pt.x)
                        list_y.append(pt.y)
                        if idx == 48:
                            start_pt_48 = pt
                        elif idx == 59:
                            list_x.append(start_pt_48.x)
                            list_y.append(start_pt_48.y)
                        elif idx == 60:
                            start_pt_60 = pt
                        elif idx == 67:
                            list_x.append(start_pt_60.x)
                            list_y.append(start_pt_60.y)
                            list_x.append(start_pt_48.x)
                            list_y.append(start_pt_48.y)

                pts = np.vstack((list_x, list_y)).astype(np.int32).T
                # mask = cv2.fillPoly(mask, [pts], (0,0,255),8,0)
                mmcolor = {
                    "MM01": [163, 74, 70],
                    "MM02": [175, 26, 20],
                    "MM03": [174, 92, 96],
                    "MM04": [166, 53, 71],
                    "MM05": [148, 33, 40],
                    "MM06": [209, 37, 85],
                    "MM07": [121, 31, 31],
                    "MM08": [167, 47, 55],  # 01
                }
                [r, g, b] = mmcolor[aim]
                color_now = [b, g, r]
                # mask = cv2.fillPoly(mask, [pts], color=color_now)

                for _ in range(5):
                    pts = measure.subdivide_polygon(pts, degree=2)

                mask = cv2.fillPoly(mask, np.int32([pts]), color=color_now)

                imgColorLips = np.zeros_like(mask)
                imgColorLips[:] = b, g, r
                # mask = cv2.bitwise_and(mask,imgColorLips)
                # mask = cv2.GaussianBlur(mask,(5,5),10)
            # # alpha 为第一张图片的透明度
            # alpha = 1
            # # beta 为第二张图片的透明度
            # beta = 0.3
            # gamma = 0
            # # cv2.addWeighted 将原始图片与 mask 融合
            # mask_img = cv2.addWeighted(img, alpha, mask, beta, gamma)
            # mask_img = cv2.addWeighted(mask, alpha, img, beta, gamma)
            mask_png = mask_add_alpha_channel(mask)
            mask_png = cv2.GaussianBlur(mask_png, (15, 15), 10, 10)
            res_img = merge_img(img, mask_png, 0, h, 0, w)

            # cv2.imshow("mask", mask)
            # cv2.imshow("res_img", res_img)
            # cv2.imshow("image", img)
            res_img = del_alpha_channel(res_img)
            res_img = beauty_face(res_img)
            AddText = res_img.copy()
            cv2.putText(AddText, aim, (100, 100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 4.0, (85, 37, 209), 5)
            np.hstack([img, AddText])
            res = np.hstack([res_img, AddText])
            cv2.waitKey(1)
            print(imgfile.split('/pic1/')[1].split('_')[0], aim)
            filename = "./test/%s_%s.jpg" % (imgfile.split('pic1/')[1].split('_')[0], aim)
            cv2.imwrite(filename, AddText)


# camera.release()
# cv2.destroyAllWindows()

for i in os.listdir(r"D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\pic1"):
    i = "D:/github/1/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/upload/pic1/"+i

    coloring(i)
    print(i)
