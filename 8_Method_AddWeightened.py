'''Bukan Add biasa
tapi melainkan add yang pake proporsi image 1 berapa persen, image 2 berapa persen'''

import cv2
import numpy as np


img = cv2.imread('D:\A LEARN\Image Processing\OpenCV India Perkenalan\Gambar\el.jpg',1)
logo = cv2.imread('D:\A LEARN\Image Processing\OpenCV India Perkenalan\Gambar\opencv.png')

img = cv2.resize(img, (512,512))
logo = cv2.resize(logo, (512,512))

gabung = cv2.addWeighted(img, 0.5, logo, 0.5, 0)

'''Jumlah dari alpha tambah beta = 1'''

cv2.imshow('gabung', gabung)
cv2.waitKey()
cv2.destroyAllWindows()