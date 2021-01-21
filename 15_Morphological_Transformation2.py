import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('D:\A LEARN\Image Processing\OpenCV India Perkenalan\Gambar\smarties.jpg', 0)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)


kernal = np.ones((30, 30), np.uint8)


dilation = cv.dilate(mask, kernal, iterations=2)   #dilation --> melebar
erosion = cv.erode(mask, kernal, iterations=2)     #erosion --> mengikis
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing']
images = [img, mask, dilation, erosion, opening, closing]


for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()