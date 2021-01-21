'''Perbandingan Image Gradient dan Canny dalam Gambar'''


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/el.jpg', 0)

#laplacian method
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))


#sobelX dan sobelY
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))


#sobelCombine
sobelCombine = cv.bitwise_or(sobelX, sobelY)

#canny
Canny = cv.Canny(img, 100, 200)


images = [img, lap, sobelX, sobelY, sobelCombine, Canny]
titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombine', 'canny']



for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.title(titles[i])
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()

