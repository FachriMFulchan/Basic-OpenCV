import numpy as np
import cv2

#koordinatnya mengacu pada cartesius

img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 1)

#membuat garis
cv2.line(img, (0,0), (255,255), (68,105,54), 10) #54, 105, 68
cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 10) #54, 105, 68


'''Untuk membuat line digunakan fungsi cv2.line
cv2.line(img, titik point 1, titik point 2, warna, thickness)
warna tuh pake format BGR
'''

#membuat rectangle
cv2.rectangle(img, (384,0), (510,128),(0,0,255), 5)
cv2.rectangle(img, (250,0), (350,128),(0,255,0), -1) #kalo thickness = -1 jadi ngefill warna

'''parameter syntax nya mirip kaya line'''


#membuat circle
cv2.circle(img, (447,63), 63, (255,0,0), -1 )



#menulis teks
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 5, cv2.LINE_AA)


#polyline
# cv2.polylines()

#ellipse
# cv2.ellipse()

#dll


cv2.imshow('gambar lena', img)
cv2.waitKey(0)
cv2.destroyAllWindows()