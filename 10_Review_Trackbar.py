import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

#Trackbar warna
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

#Trackbar switch
cv.createTrackbar('switch', 'image', 0, 1, nothing)


while True:
    cv.imshow('image', img)
    k = cv.waitKey(1)

    if k == 27:
        break

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    switch = cv.getTrackbarPos('switch', 'image')

    if switch == 0:
        img[:] = 0
    
    else:
        img[:] = [b,g,r]


cv.destroyAllWindows()