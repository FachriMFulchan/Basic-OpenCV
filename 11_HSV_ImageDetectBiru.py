import numpy as np
import cv2

def nothing(x):
    pass

while True:
    frame = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/opencv.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b = np.array((110, 50, 50))
    u_b = np.array((130, 255, 255))

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', res)


    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()