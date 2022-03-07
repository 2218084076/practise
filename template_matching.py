import cv2 as cv
import numpy as np
import show_record


# img_rgb = cv.imread('templates/record_temp.png')
def match(status):

    aim_x,aim_y =None,None

    img_rgb = cv.imread(show_record.get_android_img())
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    if status is None:
        print('missing info')
        return
    if status == 'exsitence':
        path = 'templates/exsitence.png'

    if status == 'add bar':
        path = 'templates/add bar.png'

    template = cv.imread(path, 0)
    w, h = template.shape[::-1]
    print("this", w, h)
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        x = int(pt[0] + w / 2)
        y = int(pt[1] + h / 2)
        aim_x = int(x / 644 * 1080)
        aim_y = int(y / 1430 * 2400)

    if aim_x is not None and aim_y is not None:
        print('found x y')
        return aim_x, aim_y
    else:
        print('x,y is none')
        return None,None
    # print(x,900-y)
    # print(w,pt[1])


# phone size =1080x2400
# mac 1440x900
if __name__ == '__main__':
    x,y=match('exsitence')
    print('final:',x,y)

    # cv.imwrite('res.png',img_rgb)
