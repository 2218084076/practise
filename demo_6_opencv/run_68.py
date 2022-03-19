import cv2
import dlib
import numpy as np

camera = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./data/dlib/shape_predictor_68_face_landmarks.dat")

while True:
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret:
        faces = detector(gray,0)
        for face in faces:
            landmarks = predictor(gray,face)
            x1,y1 = face.left(),face.top()
            x2,y2 = face.right(),face.bottom()
            print('[x1:%s,y1:%s]'%(x1,y1))
            print('[x2:%s,y2:%s]\n'%(x2,y2))
            for n in range(68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)
        cv2.imshow("camera",frame)
        cv2.waitKey(1)
camera.release()
cv2.destroyAllWindows()