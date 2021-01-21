'''Diterapin pada gambar Trackbarnya'''


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def nothing(x):
    print (x)

cv.namedWindow('Tracking')

cv.createTrackbar('TH1', 'Tracking', 0, 255, nothing)
cv.createTrackbar('TH2', 'Tracking', 0, 255, nothing)

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/train.jpg', 0)


while True :
    th1 = cv.getTrackbarPos('TH1', 'Tracking')
    th2 = cv.getTrackbarPos('TH2', 'Tracking')

    
    canny = cv.Canny(img, th1, th2)

    cv.imshow('image', img)
    cv.imshow('Canny', canny)

    k = cv.waitKey(1)
    if k == ord('q'):
        break

cv.destroyAllWindows()
        