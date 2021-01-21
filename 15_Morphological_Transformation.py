import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv


img = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/smarties.jpg', 0)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones([4,4], np.uint8)

dilation = cv.dilate(mask, kernal, iterations=5)


titles = ['image', 'mask', 'dilation']
images = [img, mask, dilation]


for i in range(3):
    plt.subplot(1,3, i+1)
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    plt.imshow(images[i], 'gray')

plt.show()