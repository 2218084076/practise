#1.该代码用于提取人脸68个关键点
#2.并提取嘴部mask
# coding=utf-8

import cv2
import dlib
import numpy as np


# JAW_POINTS = list(range(0, 17))
# FACE_POINTS = list(range(17, 68))
# BROW_POINTS = list(range(17, 27))
# NOSE_POINTS = list(range(27, 36))
# EYE_POINTS = list(range(36, 48))
# MOUTH_POINTS = list(range(48, 61))


def empty(a):
    pass

cv2.namedWindow('BGR')
cv2.resizeWindow('BGR', 640, 240)
cv2.createTrackbar('Blue', 'BGR', 0, 255, empty)
cv2.createTrackbar('Green', 'BGR', 0, 255, empty)


def createBox(img, points, scale=5, masked=False, cropped=True):
    if masked:
        mask = np.zeros_like(img)
        mask = cv2.fillPoly(mask, [points], (255, 255, 255))
        img = cv2.bitwise_and(img, mask)
        cv2.imshow('Mask',img)

    if cropped:
        bbox = cv2.boundingRect(points)
        x, y, w, h = bbox
        imgCrop = img[y:y + h, x:x + w]
        imgCrop = cv2.resize(imgCrop, (0, 0), None, scale, scale)
        return imgCrop
    else:
        return mask

camera = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("D:/github/hotpoor_autoclick_xhs/demo_6_opencv/data/dlib/shape_predictor_68_face_landmarks.dat")

while True:
    # image
    # 1 读入图片并进行人脸关键点检测
    img = cv2.imread('1.jpg')

    img = cv2.resize(img,(0,0),None,0.5,0.5)
    imgOriginal = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(imgGray)

    for face in faces:
        x1,y1 = face.left(),face.top()
        x2,y2 = face.right(),face.bottom()
        imgOriginal = cv2.rectangle(img, (x1,y1),(x2,y2),(0,255,0),2)
        landmarks = predictor(imgGray,face)
        myPoints =[]
        for n in range(68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            myPoints.append([x,y])
            cv2.circle(imgOriginal,(x,y),5,(50,50,255),cv2.FILLED)
            cv2.putText(imgOriginal,str(n),(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.9,(0,0,255),1)

        myPoints = np.array(myPoints)

        imgLeftEye = createBox(img,myPoints[36:42],8)
        cv2.imshow('LeftEye',imgLeftEye)
        # 2 嘴唇区域mask提取
        imgLips = createBox(img,myPoints[48:61],8,masked=True,cropped=False)

        imgColorLips = np.zeros_like(imgLips)
        # 3 创建滑动条，以及获取滑动条的值，嘴唇区域上色并与原图融合
        b = cv2.getTrackbarPos('Blue','BGR')
        g = cv2.getTrackbarPos('Green','BGR')
        r = cv2.getTrackbarPos('Red','BGR')
        imgColorLips[:] = b,g,r
        imgColorLips = cv2.bitwise_and(imgLips,imgColorLips)
        imgColorLips = cv2.GaussianBlur(imgColorLips,(7,7),10)

        #color_image
        imgColorLips = cv2.addWeighted(imgOriginal,1,imgColorLips,0.4,0)

        #gray_image
        imgOriginalGray = cv2.cvtColor(imgOriginal,cv2.COLOR_BGR2GRAY)
        imgOriginalGray = cv2.cvtColor(imgOriginalGray,cv2.COLOR_GRAY2BGR)
        imgColorLips = cv2.addWeighted(imgOriginalGray,1,imgColorLips,0.4,0)
        cv2.imshow('BGR',imgColorLips)
        cv2.imshow('Lips',imgLips)

        print(myPoints)

    cv2.imshow("Original",imgOriginal)
    cv2.waitKey(1)

# while True:
#     ret, img = camera.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     if ret:
#         dets = detector(gray, 0)
#         h, w, c = img.shape
#         mask = np.zeros((h, w), dtype=np.uint8)
#         for face in dets:
#             shape = predictor(img, face)  # 寻找人脸的68个标定点
#             # 遍历所有点，打印出其坐标，并圈出来
#             for idx,pt in enumerate(shape.parts()):
#                 pt_pos = (pt.x, pt.y)
#                 cv2.circle(img, pt_pos, 2, (0, 255, 0), 1)
#                 font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
#                 cv2.putText(img,str(idx),pt_pos,font,0.4,(0,0,255),1,cv2.LINE_AA)
#             cv2.imshow("image", img)
#
#             h, w, c = img.shape
#             # 手工绘制ROI区域
#             mask = np.zeros((h, w), dtype=np.uint8)
#
#             list_x = []
#             list_y = []
#             start_pt = None
#             for idx, pt in enumerate(shape.parts()):
#                 # if idx >= 48 and idx <= 59:
#                 if idx >= 48 and idx <= 67:
#                     list_x.append(pt.x)
#                     list_y.append(pt.y)
#                     if idx == 48:
#                         start_pt = pt
#                     if idx == 59:
#                         list_x.append(pt.x)
#                         list_y.append(pt.y)
#                         list_x.append(start_pt.x)
#                         list_y.append(start_pt.y)
#
#             pts = np.vstack((list_x, list_y)).astype(np.int32).T
#             cv2.fillPoly(mask, [pts], (125), 8, 0)
#         cv2.imshow("mask", mask)
#         cv2.imshow("image", img)
#         cv2.waitKey(1)
#
# camera.release()
# cv2.destroyAllWindows()

