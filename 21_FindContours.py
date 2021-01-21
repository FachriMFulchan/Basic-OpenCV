import numpy as np
import cv2


img = cv2.imread('D:\A LEARN\Image Processing\OpenCV India Perkenalan\Gambar\opencv.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 180, 255, cv2.THRESH_BINARY_INV)          #Threshold taulah gimana
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)      #nah ini parameter normalnya


cv2.drawContours(img, contours, -1, (127,255,0), 3)
#-1 tuh nge draw semua kontur
#kalo 0,1,2,3,4 dst itu konstur sesuai indeks

#FindContours akan ngefeedback 2 inputan yaitu kontur dan hierarchy
#yang dipake adalah kontur, hierarchy nantu lagi

cv2.imshow('Threshold', thresh)
cv2.imshow('Input', img)
cv2.imshow('Gray', img_gray)
cv2.waitKey()