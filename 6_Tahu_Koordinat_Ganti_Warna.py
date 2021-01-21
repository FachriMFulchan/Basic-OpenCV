import cv2
import numpy as np

# img = np.zeros((512,512,3))
img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 1)
a = 255
b = 255
c = 255


def click_event(event, x, y, flags, param) :
    global a,b,c #biar bisa masukkin variabel global
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (a,b,c), 1, cv2.LINE_AA)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x,y), font, 0.5, (255,0,0), 1, cv2.LINE_AA)
        cv2.imshow('image', img)

    if event == cv2.EVENT_MBUTTONDOWN:
        a = np.random.randint(0, 255)
        b = np.random.randint(0, 255)
        c = np.random.randint(0, 255)

while True:
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    k = cv2.waitKey()

    if k == ord('q'):
        break
    
cv2.destroyAllWindows()