import numpy as np
import cv2

def nothing(x):
    print (x)


img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

#Trackbar warna
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

#Trackbar Switch
cv2.createTrackbar('Switch', 'image', 0, 1, nothing)


while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1)

    if k == 27:
        break

    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    switch = cv2.getTrackbarPos('Switch', 'image')

    if switch == 0:
        img[:] = 0

    else :        
        img[:] = [b,g,r]


cv2.destroyAllWindows()