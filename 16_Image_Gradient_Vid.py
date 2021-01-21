'''Kita coba terapin ke Video'''


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #laplacian
    lap = cv.Laplacian(frame, cv.CV_64F, ksize=3)
    lap = np.uint8(np.absolute(lap))


    #sobelXY
    sobelX = cv.Sobel(frame, cv.CV_64F, 1, 0, ksize=3)
    sobelY = cv.Sobel(frame, cv.CV_64F, 0, 1, ksize=3)

    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))


    #sobelCombine
    sobelCombine = cv.bitwise_or(sobelX, sobelY)


    cv.imshow('frame', frame)
    cv.imshow('Laplacian', lap)
    cv.imshow('SobelX', sobelX)
    cv.imshow('SobelY', sobelY)
    cv.imshow('sobelCombine', sobelCombine)

    k = cv.waitKey(1)
    if k == ord('q'):
        break


cap.release()
cv.destroyAllWindows()

