import cv2 as cv
import numpy as np

img = cv.imread('D:\A LEARN\Image Processing\OpenCV India Perkenalan\Gambar\sudoku2.jpg',0)
img = cv.resize(img,(512,512))
_, th1 = cv.threshold(img, 127,255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
th4 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 511, 2)

cv.imshow('image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)

cv.waitKey()
cv.destroyAllWindows()