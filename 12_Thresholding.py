import numpy as np
import cv2

img = cv2.imread('D:\A LEARN\Image Processing\OpenCV India Perkenalan\Gambar\gradient.jpg')
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)        #nyeleksi nilai pixel misal antara 127-255, kalo bener dikasih logic 1, sisanya 0
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)    #sama aja, tapi kalo bener dikasih logic 0
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)         #dari nilai 127 sampe 255, nilai pixelnya disamain jadi 127
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)         #nilai yang kurang dari diitemin (0), sisanya dibiarin
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)     #kebalikannya



cv2.imshow('image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)

cv2.waitKey()
cv2.destroyAllWindows()