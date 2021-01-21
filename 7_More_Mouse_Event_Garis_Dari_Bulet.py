''' gini nii cara  kerjanya
nge klick sekali muncul bulet kecil
nge klick dua kali muncul bulet kecil
kemudian muncul garis yang mengubungkan kedua bulet tersebut'''

import cv2
import numpy as np


img = np.zeros((1024, 780, 3))


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,255,0), -1)
        points.append((x,y))
        print (points)
        
        cv2.imshow('image', img)

        #versi 1
        if len(points) >=  2:
            cv2.line(img, points[-2], points[-1],(0,255,0), 3, cv2.LINE_AA)
            cv2.imshow('image', img)

        #versi 2
        # if len(points) >= 2:
        #     cv2.line(img, points[0], points[1],(0,255,0), 3, cv2.LINE_AA)
        #     points = []
        #     cv2.imshow('image', img)



cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)


cv2.waitKey()
cv2.destroyAllWindows()
