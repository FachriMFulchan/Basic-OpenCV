'''Canny Edge tuh mirip mirip sama Image Gradient
cuma noise nya lebih sedikit dan threshold nya bisa diatur'''


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 0)
canny = cv.Canny(img, 100, 200)

titles = ['image', 'kenny']
images = [img, canny]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.title(titles[i])
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()