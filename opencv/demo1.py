import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./data/dlib/shape_predictor_68_face_landmarks.dat")

capture = cv2.VideoCapture(0)
while True:
    sucess,img=capture.read()
    cv2.imshow("iLucAs",img)
    key=cv2.waitKey(50)
    if key == 27:
        cv2.destroyAllWindows()
        break
capture.release()
