import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


cap = cv.VideoCapture(0)

def nothing(x):
    print (x)

#buatTrackbar
cv.namedWindow('Tracking')
cv.createTrackbar('th1', 'Tracking', 0, 255, nothing)
cv.createTrackbar('th2', 'Tracking', 0, 255, nothing)


while True:
    th1 = cv.getTrackbarPos('th1', 'Tracking')
    th2 = cv.getTrackbarPos('th2', 'Tracking')

    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    
    #laplacian method
    lap = cv.Laplacian(frame, cv.CV_64F, ksize=3)
    lap = np.uint8(np.absolute(lap))


    #sobelX
    sobelX = cv.Sobel(frame, cv.CV_64F, 1, 0, ksize=3)
    sobelX = np.uint8(np.absolute(sobelX))


    #sobelY
    sobelY = cv.Sobel(frame, cv.CV_64F, 0, 1, ksize=3)
    sobelY = np.uint8(np.absolute(sobelY))


    #sobelCombine
    sobelCombine = cv.bitwise_or(sobelX, sobelY)


    #canny
    canny = cv.Canny(frame, th1, th2)


    cv.imshow('frame', frame)
    cv.imshow('laplacian', lap)
    cv.imshow('sobelX', sobelX)
    cv.imshow('sobelY', sobelY)
    cv.imshow('sobelCombine', sobelCombine)
    cv.imshow('Canny', canny)


    k = cv.waitKey(1)
    if k == ord ('q'):
        break

cap.release()
cv.destroyAllWindows()