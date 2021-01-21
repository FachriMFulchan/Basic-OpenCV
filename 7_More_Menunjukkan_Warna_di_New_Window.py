import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        imagecolor = np.zeros((512,512,3), np.uint8) #uint kudu wajib dipake banget
        print (blue, green, red)
        imagecolor[:] = [blue, green, red]
        cv2.imshow('color', imagecolor)
        


img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/sawah.jpg', 1)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey()
cv2.destroyAllWindows()