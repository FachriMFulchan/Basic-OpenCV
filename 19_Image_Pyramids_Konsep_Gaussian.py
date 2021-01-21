'''Konsepnya gini,
ada pyrUp untuk memperbesar 1/4 kali
ada pyrDown untuk memperkecil 1/4 kali
'''


import cv2 as cv
import numpy as np

img = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 1)
lr1 = cv.pyrDown(img)
lr2 = cv.pyrDown(lr1)
hr2 = cv.pyrUp(lr2)


cv.imshow('Image asli', img)
cv.imshow('PyrDown1', lr1)
cv.imshow('PyrDown2', lr2)
cv.imshow('PyrUp', hr2)


cv.waitKey(0)
cv.destroyAllWindows()