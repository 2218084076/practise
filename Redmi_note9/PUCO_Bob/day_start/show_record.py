import mss
import mss.tools
import time
import cv2 as cv

from setting import android_x0
from setting import android_y0
from setting import android_x1
from setting import android_y1

def get_android_img():
    starttime = time.time()
    with mss.mss() as sct:
        region = {
            "top":android_y0,
            "left":android_x0,
            "width":android_x1 - android_x0,
            "height":android_y1 - android_y0,
        }
        img = sct.grab(region)

        path_temp = "./hotpoor_autoclick_cache/record_temp.png"
        mss.tools.to_png(img.rgb,img.size,output=path_temp)
        endtime = time.time()
    return path_temp

while True:
    base_img = cv.imread(get_android_img(),0)
    # gray_img = cv.cvtColor(base_img, cv.COLOR_BGR2GRAY)
    cv.imshow("img",base_img)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("v"):
        filename = "./temp/video/video_%s.jpg"%(time.time())
        cv.imwrite(filename,base_img)
        print("video:%s"%(filename))
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
        print("list:%s"%(filename))
    elif key == ord("b"):
        filename = "./temp/black/black_%s.jpg"%(time.time())
        cv.imwrite(filename,base_img)
        print("list:%s"%(filename))
    elif key == ord("d"):
        filename = "./temp/desktop/desktop_%s.jpg"%(time.time())
        cv.imwrite(filename,base_img)
        print("list:%s"%(filename))
    elif key == ord("c"):
        filename = "./temp/close/close_%s.jpg"%(time.time())
        cv.imwrite(filename,base_img)
        print("list:%s"%(filename))
    elif key == ord("e"):
        filename = "./temp/share/share_%s.jpg"%(time.time())
        cv.imwrite(filename,base_img)
        print("list:%s"%(filename))
    elif key == ord("f"):
        filename = "./temp/footer/footer_%s.jpg"%(time.time())
        cv.imwrite(filename,base_img)
        print("list:%s"%(filename))


cv.destroyAllWindows()
