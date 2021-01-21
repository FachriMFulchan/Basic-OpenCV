'''
Region Of Interest
jadi bagian bagian yag diseleksi sesuai kemauan
'''


import numpy as np
import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print (x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)

        cv2.putText(img, strXY, (x,y), font, 0.5, (0,0,255), 1, cv2.LINE_AA )
        cv2.imshow('image', img)


img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/el.jpg', 1)


ball = img[523:640,508:607]
img[523:640, 103:202] = ball
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
cv2.waitKey()

cv2.destroyAllWindows()