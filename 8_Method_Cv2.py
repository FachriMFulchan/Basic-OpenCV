'''
img.shape
img.size
img.dtype
'''


import cv2
import numpy as np


img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/messi.jpg',1)



print(img.shape) #returns a tuple of rows, columns and chanels
print(img.size) #return total number of pixel (row*columns*chanell)
print(img.dtype) #return image datatype is obtained

b,g,r = cv2.split(img)  #ngesplit semua bgr dalam setiap pixel di gambar
img = cv2.merge((b,g,r)) #nyatuin semua bgr perpixel jadi gambar lagi

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()