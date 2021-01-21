import cv2
import numpy as np



def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print (x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255, 0), 1, cv2.LINE_AA)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x,y), font, 0.5, (0,255, 0), 1)
        cv2.imshow('image', img)

    '''Di string nya jan pake coma(,)
    pake concat aja (+)
    soalnya ga reliable pake , maa'''

'''Soalnya nanti kalo pake , terus ada castingan bakal
a = 1
print ('hayu', str(a))
bakal jadi: hayu, 1

kalo concat kan
print ('hayu + str(a))
bakal jadi : hayu 1
'''



img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 1)

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()


