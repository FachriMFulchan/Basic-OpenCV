'''Ada 4 jenis metode image Gradient
- Laplacian
- Sobel X
- Sobel Y
- SobelCombine
'''


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('D:/A LEARN/Image Processing/OpenCV India Perkenalan/Gambar/el.jpg', 0)

#laplacian method
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)  #jadi 64 bit float yang support bil. negatif /// Ksize teh ketelitian kernel nya 
lap = np.uint8(np.absolute(lap))  #terus diambil nilai abslolute nya /// di convert lagi ke int 8 bit


#sobelX dan sobelY
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)  #dx =1, dy = 0
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3) #dx =0, dy = 1

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))



#sobelCombine
sobelCombine = cv.bitwise_or(sobelX, sobelY)



#sobelCombine2 (jelek)
sobelCombine2 = cv.Sobel(img, cv.CV_64F, 1, 1, ksize=3)
sobelCombine2 = np.uint8(np.absolute(sobelCombine2))



images = [img, lap, sobelX, sobelY, sobelCombine, sobelCombine2]
titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombine', 'sobelCombine2']


cv.imshow('Laplacian', lap)
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.title(titles[i])
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()