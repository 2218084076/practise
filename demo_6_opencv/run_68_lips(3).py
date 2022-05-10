#1.该代码用于提取人脸68个关键点
#2.并提取嘴部mask
# coding=utf-8

import cv2
import dlib
import numpy as np
import time


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


def mask_add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """
    b_channel, g_channel, r_channel = cv2.split(img) # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 # 创建Alpha通道
 
    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel)) # 融合通道
    
    # print(len(img_new),len(img_new[0]),img_new[0][0])
    h = len(img_new)
    w = len(img_new[0])
    for col in range(0,h):
        for row in range(0,w):
            [g,b,r,alpha] = img_new[col][row]
            if r==0 and g==0 and b==0:
                img_new[col][row][3]=0
            else:
                img_new[col][row][3]=int(255*0.3)
    return img_new
def add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """
 
    b_channel, g_channel, r_channel = cv2.split(img) # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 # 创建Alpha通道
 
    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel)) # 融合通道
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
    alpha_png = png_img[yy1:yy2,xx1:xx2,3] / 255.0
    alpha_jpg = 1 - alpha_png
    
    # 开始叠加
    for c in range(0,3):
        jpg_img[y1:y2, x1:x2, c] = ((alpha_jpg*jpg_img[y1:y2,x1:x2,c]) + (alpha_png*png_img[yy1:yy2,xx1:xx2,c]))
 
    return jpg_img
# is_true = True
# while is_true:
# img = camera.read()
aim_list = ["mm01","mm02","mm03","mm04","mm05","mm06","mm07","mm08"]
for aim in aim_list:
    ret = True

    if ret:
        dets = detector(gray, 0)
        h, w, c = img.shape
        print(h,w,c)
        # mask = np.zeros((img.shape), dtype=np.uint8)
        mask = np.zeros((img.shape), dtype=np.uint8)
        for face in dets:
            shape = predictor(img, face)  # 寻找人脸的68个标定点
            # 遍历所有点，打印出其坐标，并圈出来
            for idx,pt in enumerate(shape.parts()):
                pt_pos = (pt.x, pt.y)
                # cv2.circle(img, pt_pos, 2, (0, 255, 0), 1)
                font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
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

            pts = np.vstack((list_x, list_y)).astype(np.int32).T
            # mask = cv2.fillPoly(mask, [pts], (0,0,255),8,0)
            mmcolor={
                "mm01":[177,88,71],
                "mm02":[162,75,41],
                "mm03":[179,103,70],
                "mm04":[127,5,26],
                "mm05":[161,68,64],
                "mm06":[169,54,68],
                "mm07":[121,31,31],
                "mm08":[167,47,55],#01
                "blue":[0,0,255],
            }
            [r,g,b] = mmcolor[aim]
            color_now = [b,g,r]
            mask = cv2.fillPoly(mask, [pts], color=color_now)
            imgColorLips = np.zeros_like(mask)
            imgColorLips[:] = b,g,r
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
        mask_png = cv2.GaussianBlur(mask_png,(5,5),10)
        res_img = merge_img(img, mask_png, 0, h, 0, w)

        cv2.imshow("mask", mask)
        cv2.imshow("res_img", res_img)
        cv2.imshow("image", img)
        cv2.waitKey(1)
        filename = "./test/result_%s.jpg"%(time.time())
        cv2.imwrite(filename,res_img)

# camera.release()
# cv2.destroyAllWindows()

