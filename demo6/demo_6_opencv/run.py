import cv2
print("""
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
opencv 自带数据集模型
https://github.com/opencv/opencv/tree/master/data/haarcascades
    """)
camera = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_alt2.xml')
def detect_face(img):
    #将测试图像转换为灰度图像，因为opencv人脸检测器需要灰度图像
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = img
    #加载OpenCV人脸检测分类器Haar
    global face_cascade
    #检测多尺度图像，返回值是一张脸部区域信息的列表（x,y,宽,高）
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    # 如果未检测到面部，则返回原始图像
    if (len(faces) == 0):
        return 0, None, None
    #目前假设只有一张脸，xy为左上角坐标，wh为矩形的宽高
    (x, y, w, h) = faces[0]
    #返回图像的正面部分
    # return gray[y:y + w, x:x + h], faces[0], True
    return len(faces),faces,True
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (128, 128, 0), 3)
    return img
while True:
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret:
        face_num, faces, has_face = detect_face(gray)
        if has_face:
            print("face_num:",face_num)
            for face in faces:
                face_rect = face
                (x, y, w, h) = face_rect
                x0 =x
                y0 = int(y+h/2)
                gray_face = frame[y0:y+h,x:x+w]
                frame = draw_rectangle(frame,face_rect)
        cv2.imshow("camera",frame)
        cv2.waitKey(1)
camera.release()
cv2.destroyAllWindows()