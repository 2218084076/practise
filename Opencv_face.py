import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def create_rgb_hist(image):
    """"创建 RGB 三通道直方图（直方图矩阵）"""
    h, w, c = image.shape
    # 创建一个（16*16*16,1）的初始矩阵，作为直方图矩阵
    # 16*16*16的意思为三通道每通道有16个bins
    rgbhist = np.zeros([16 * 16 * 16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            # 人为构建直方图矩阵的索引，该索引是通过每一个像素点的三通道值进行构建
            index = int(b / bsize) * 16 * 16 + int(g / bsize) * 16 + int(r / bsize)
            # 该处形成的矩阵即为直方图矩阵
            rgbhist[int(index), 0] += 1
    plt.ylim([0, 10000])
    plt.grid(color='r', linestyle='--', linewidth=0.5, alpha=0.3)
    return rgbhist


def hist_compare(hist1, hist2):
    """直方图比较函数"""
    '''# 创建第一幅图的rgb三通道直方图（直方图矩阵）
    hist1 = create_rgb_hist(image1)
    # 创建第二幅图的rgb三通道直方图（直方图矩阵）
    hist2 = create_rgb_hist(image2)'''
    # 进行三种方式的直方图比较
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离：%s, 相关性：%s, 卡方：%s" % (match1, match2, match3))


def handle_img(img):
    img = cv.resize(img, (100, 100))
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    img[:, :, 2] = cv.equalizeHist(img[:, :, 2])
    img = cv.cvtColor(img, cv.COLOR_HSV2BGR)
    return img


img1 = cv.imread("1.jpg")
img1 = handle_img(img1)
cv.imshow("img1", img1)

img2 = cv.imread("2.jpg")
img2 = handle_img(img2)
cv.imshow("img2", img2)

img3 = cv.imread("3.jpg")
img3 = handle_img(img3)
cv.imshow("img3", img3)

img4 = cv.imread("4.jpg")
img4 = handle_img(img4)
cv.imshow("img4", img4)

hist1 = create_rgb_hist(img1)
hist2 = create_rgb_hist(img2)
hist3 = create_rgb_hist(img3)
hist4 = create_rgb_hist(img4)

plt.subplot(1, 4, 1)
plt.title("hist1")
plt.plot(hist1)
plt.subplot(1, 4, 2)
plt.title("hist2")
plt.plot(hist2)
plt.subplot(1, 4, 3)
plt.title("hist3")
plt.plot(hist3)
plt.subplot(1, 4, 4)
plt.title("hist4")
plt.plot(hist4)

hist_compare(hist1, hist2)
hist_compare(hist2, hist3)
hist_compare(hist3, hist4)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()