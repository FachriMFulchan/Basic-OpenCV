import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/gradient.jpg', 0)
img2 = cv.cvtColor(img, cv.COLOR_RGB2BGR)
_, th1 = cv.threshold(img2, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img2, 127, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img2, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img2, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img2, 127, 255, cv.THRESH_TOZERO_INV)

#mending pake matplotlib
titles = ['Original image', 'Binary', 'Binary Inv', 'Trunc', 'To Zero', 'To Zero Inv']
images = [img, th1, th2, th3, th4, th5]


for i in range(6):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    
plt.show()


#instead to use this
# cv.imshow('image', img)
# cv.imshow('th1', img)
# cv.imshow('th2', img)
# cv.imshow('th3', img)
# cv.imshow('th4', img)
# cv.imshow('th5', img)

cv.waitKey()
cv.destroyAllWindows()


