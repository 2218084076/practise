import cv2
import numpy as np
import dlib
import time,os
from PIL import Image, ImageFilter
from skimage import measure,data,color
from fourfaces import x4faces
from twofaces import x2faces
from faces import x3faces


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


def add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """

    b_channel, g_channel, r_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道

    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))  # 融合通道
    return img_new


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
    temp4 = cv2.subtract(cv2.add(cv2.add(temp3, temp3), src), (30, 30, 30, 255))

    dst = cv2.addWeighted(src, p, temp4, 1 - p, 0.0)
    dst = cv2.add(dst, (10, 10, 10, 255))
    return dst
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./data/dlib/shape_predictor_68_face_landmarks.dat")

aim_list = ["MM01","MM02","MM03","MM04","MM05","MM06","MM07","MM08",'Mac chili','Mac Marrakesh','Mac Ruby woo','Mac Dubonnet','YSL 12 Corail','YSL 80 Chili']
list = os.listdir(r'D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\pic')
pics =[]
print(list)
for i in list:
    if 'jpeg' in i or 'jpg' in i:
        pics.append(i)

print(pics)
for i1 in pics:
    with open(r"D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\total.txt")as f:
        count = f.readline()
        f.close()
    print(count)
    print(count)
    print(count)
    print(count)
    print(i1)
    # # ----ryan
    #
    # img = cv2.imread('pics/%s'%i)
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # face = detector(imgGray)
    # for face in face:
    #     x1, y1 = face.left(), face.top()
    #     x2, y2 = face.right(), face.bottom()
    #     landmarks = predictor(imgGray, face)
    # h = y2 - y1
    # w = x2 - x1
    # x = int(w - (0.75 * h))
    # if y1 - x < 0:
    #     y2 += x
    # else:
    #     y1 -= 0.5 * x
    #     y2 += 0.5 * x
    # imgCrop = img[int(y1):int(y2), x1:x2]
    # cv2.imwrite("pics/%s"%i, imgCrop)
    #
    # # -------end
    for aim in aim_list:
        img = cv2.imread(r'D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\pic\%s' % i1)
        cv2.imwrite('afterWork/MM00.jpg', img)
        cv2.imwrite('afterWork/original/%s.jpg'%count, img)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector(imgGray)
        if len(faces) > 0:
            face = faces[0]
        #for face[0] in faces:
            x1,y1 = face.left(),face.top()
            x2,y2 = face.right(),face.bottom()
            #imgOriginal = cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            landmarks = predictor(imgGray,face)
            myPoints = []

            for n in range(68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                # # add text on roi
                # cv2.circle(img,(x,y),3,(50,50,255),cv2.FILLED)
                # cv2.putText(img,str(n),(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(0,0,255),1)
                myPoints.append([x,y])

            # -- set ROI
            y1 = myPoints[60][1]
            y2 = myPoints[57][1]
            x1 = myPoints[58][0]
            x2 = myPoints[56][0]
            # --- crop lip
            lipPoints = []
            startPoint = []
            endPoint=[]
            for i in range(68):
                if i ==48:
                    startPoint = myPoints[i]
                if i >=48 and i<=68:
                    lipPoints.append(myPoints[i])
                if i ==59:
                    lipPoints.append(startPoint)
                if i ==60:
                    endPoint= myPoints[i]
                if i == 67:
                    lipPoints.append(endPoint)
                    lipPoints.append(startPoint)
            lipPoints = np.array(lipPoints)
            for _ in range(5):
                lipPoints = measure.subdivide_polygon(lipPoints, degree=2)
            lipPoints = np.int32(lipPoints)
            #mask = cv2.fillPoly(mask, np.int32([pts]), color=color_now)

            mask = np.zeros(img.shape, dtype=np.uint8)
            roi_corners = np.array([lipPoints], dtype=np.int32)

            channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
            ignore_mask_color = (255,) * channel_count
            cv2.fillPoly(mask, roi_corners, ignore_mask_color)
            # # from Masterfool: use cv2.fillConvexPoly if you know it's convex
            masked_image = cv2.bitwise_and(img, mask)
            # ---end
            # ---crop lip
            myPoints1 = np.array(lipPoints)
            bbox = cv2.boundingRect(myPoints1)
            x, y, w, h = bbox
            imgCrop = masked_image[y:y + h, x:x + w]
            # #--- crop a box on lower lip
            # #box = img[y1:y2, x1:x2]

            # --- end
            # # -- find most common color
            # box = cv2.cvtColor(box, cv2.COLOR_BGR2RGB)
            # unique, counts = np.unique(box.reshape(-1, 3), axis=0, return_counts=True)
            # box[:, :, 0], box[:, :, 1], box[:, :, 2] = unique[np.argmax(counts)]
            # mostCommon = unique[np.argmax(counts)]
            # print('the most common color on lower lip is :' + str(mostCommon))
            # box = cv2.cvtColor(box, cv2.COLOR_RGB2BGR)
            # # show_img_compar(img, img_temp)
            # # -- end

            # # ---create average color mask
            # mask = np.zeros((100, 100, 3), dtype=np.uint8)
            # mask[:] = (mostCommon[2], mostCommon[1], mostCommon[0])
            # # create puco color mask
            # puco = np.zeros((100, 100, 3), dtype=np.uint8)
            # puco[:] = (20, 21, 200)
            #
            # # to HSV
            # mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
            # imgCrop = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2HSV)
            # puco = cv2.cvtColor(puco, cv2.COLOR_BGR2HSV)
            # # substract values
            # a1, a2, a3 = puco[1][1]
            # b1, b2, b3 = mask[1][1]
            # print(a1, a2, a3)
            # print(b1, b2, b3)
            # h = int(a1) - int(b1)
            # s = int(a2) / int(b2)
            # v = int(a3) / int(b3)
            # print(h, s, v)
            #
            # # aply colors
            #
            # for x in imgCrop:
            #     for y in x:
            #         if y[1] ==0 and y[2]==0 and y[0]==0:
            #             continue
            #         else:
            #             if y[1] * s <= 255:
            #                 y[1] *= s
            #             else:
            #                 y[1] = 255 - ((y[1] * s) - 255)
            #             #y[2] *= v
            #             # lets fucking go baby!!!!!!!!!!!!!
            # imgCrop = cv2.cvtColor(imgCrop, cv2.COLOR_HSV2BGR)
            #concatenation 1
            imgl = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2BGRA)

            cv2.imwrite('3.png', imgl)

            # delete black background
            img1 = Image.open('3.png')
            img1 = img1.convert("RGBA")
            datas = img1.getdata()
            newData = []
            mmcolor = {
                "MM01": [139, 41, 37],
                "MM02": [136, 19, 14],
                "MM03": [119, 49, 47],
                "MM04": [124, 35, 41],
                "MM05": [110, 15, 7],
                "MM06": [136, 24, 38],
                "MM07": [121, 31, 31],
                "MM08": [167, 47, 55],  # 01
                "blue": [0, 0, 255],
                'Mac chili': [167, 30, 10],
                'Mac Marrakesh': [155, 57, 30],
                'Mac Ruby woo': [152, 34, 42],
                'Mac Dubonnet': [149, 56, 49],
                'YSL 12 Corail': [225, 39, 62],
                'YSL 80 Chili': [157, 20, 30],
                'test': [191, 123, 128],
                'after': [200, 21, 20]
            }
            [r, g, b] = mmcolor[aim]

            for item in datas:
                if item[0] <= 55 and item[1] <= 55 and item[2] <= 55:
                    newData.append((255, 255, 255, 0))
                else:
                    # item =list(item)
                    # item[3] = int(255*0.3)
                    # item = tuple(item)
                    # newData.append(item)
                    newData.append((r,g,b,int(255*0.4)))

            img1.putdata(newData)
            #img1 = img1.filter(ImageFilter.GaussianBlur(radius=1))
            img1.save("4.png", "PNG")
            imgl = cv2.imread('4.png', cv2.IMREAD_UNCHANGED)
            imgl = cv2.GaussianBlur(imgl,( 11, 11), 10)
            # concate final
            #imgResult = cvzone.overlayPNG(img, imgl, [bbox[0], bbox[1]])
            imgResult = merge_img(img,imgl,y,y+h,x,x+w)
            #imgResult = beauty_face2(imgResult)
            cv2.putText(imgResult, aim, (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (186, 38, 186), 4)
            #imgResult = cv2.bilateralFilter(imgResult,7,50,50)
            cv2.imwrite('afterWork/%s.jpg'%aim,imgResult)
    x3faces(int(count))

    with open(r"D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\total.txt",'w')as f:
        f.write(str(int(count)+1))
        f.close()




# concatenation (failed)
# maskImg = np.zeros_like(img)
# maskImg = cv2.fillPoly(maskImg,[myPoints1],(255,255,255))
# maskImg = cv2.bitwise_not(maskImg)
# after = cv2.bitwise_and(maskImg,img)
# after = cv2.bitwise_or(after,masked_image)

