import mss
import mss.tools
import time
import cv2 as cv

android_x0 = 0 #752   # left x
android_x1 =322 #1165   # right x 806

android_y0 = 900-845 #90
android_y1 = 900-130 #987

def get_android_img():
    starttime = time.time()
    with mss.mss() as sct:
        region = {
            "top":android_y0,
            "left":android_x0,
            "width":android_x1 - android_x0,
            "height":android_y1 - android_y0,
        }
        print('this is monitor width')
        print(android_x1 - android_x0)
        print('this is monitor height')
        print(android_y1 - android_y0)
        img = sct.grab(region)

        path_temp = "templates/record_temp.png"
        mss.tools.to_png(img.rgb,img.size,output=path_temp)

    return path_temp



if __name__ == '__main__':
    while True:
        base_img = cv.imread(get_android_img(),0)
        # gray_img = cv.cvtColor(base_img, cv.COLOR_BGR2GRAY)
        cv.imshow("img",base_img)
        key = cv.waitKey(1)
        if key == ord("q"):
            break
        elif key == ord("n"):
            filename = "./temp/news/news_%s.jpg"%(time.time())
            cv.imwrite(filename,base_img)
            print("news:%s"%(filename))
        elif key == ord("h"):
            filename = "./temp/home/home_%s.jpg"%(time.time())
            cv.imwrite(filename,base_img)
            print("home:%s"%(filename))
        elif key == ord("s"):
            filename = "./temp/search/search_%s.jpg"%(time.time())
            cv.imwrite(filename,base_img)
            print("search:%s"%(filename))
        elif key == ord("l"):
            filename = "./temp/list/list_%s.jpg"%(time.time())
            cv.imwrite(filename,base_img)
            print("list:%s"%(filename))
        elif key == ord("p"):
            filename = "./temp/shop/shop_%s.jpg"%(time.time())
            cv.imwrite(filename,base_img)
            print("shop:%s"%(filename))
    cv.destroyAllWindows()
