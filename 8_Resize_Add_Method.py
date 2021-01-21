import cv2
import numpy as np


img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/el.jpg',1)
logo = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/opencv.png')

#sebelum digabung di resize duls
img = cv2.resize(img, (512,512))
logo = cv2.resize(logo, (512,512))

#baru di add
gabung = cv2.add(logo, img)


cv2.imshow('image gabung', gabung)
cv2.waitKey()
cv2.destroyAllWindows()