'''Biar kita ga ribet gitu pyrdown terus terusan
yaudah pake for aja'''

import cv2 as cv
import numpy as np

img = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 1)
layer = img.copy()
gp = [layer]


for i in range (6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow(str(i), layer)

cv.imshow('Image asli', img)
cv.waitKey(0)
cv.destroyAllWindows()


