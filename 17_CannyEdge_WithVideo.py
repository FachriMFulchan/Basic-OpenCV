'''Sekarang coba kita terapin Trackbar di Video'''


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

def nothing (x):
    print (x)

cv.namedWindow('Tracking')
cv.createTrackbar('th1', 'Tracking', 0, 255, nothing)
cv.createTrackbar('th2', 'Tracking', 0, 255, nothing)


while True:
    th1 = cv.getTrackbarPos('th1', 'Tracking')
    th2 = cv.getTrackbarPos('th2', 'Tracking')

    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    canny = cv.Canny(frame, th1, th2)

    cv.imshow('frame', frame)
    cv.imshow('Canny', canny)

    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
