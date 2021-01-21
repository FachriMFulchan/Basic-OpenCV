import numpy as np
import cv2

def nothing(x):
    print (x)


img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image') #membuat windownya

#membuat trackbar, tapi belum bisa dipake
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)




while True :
    cv2.imshow('image', img)
    k = cv2.waitKey(1)

    if k == 27:
        break

    #manggil trackbar biar valuenya bisa dipake
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')

    img[:] = [b,g,r]

cv2.destroyAllWindows()