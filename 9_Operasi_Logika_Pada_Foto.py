import numpy as np
import cv2

img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/el.jpg',1)

bitNot = cv2.bitwise_not(img)

cv2.imshow('image', bitNot)
cv2.waitKey()
cv2.destroyAllWindows()