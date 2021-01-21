import cv2 as cv
import numpy as np

apple = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/apple.jpg', 1)
orange = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/orange.jpg', 1)
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))




#Generate Gaussian Pyramid For Apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
    cv.imshow(str(i), apple_copy)

#Generate Laplacian Pyramids For Apple
apple_copy = gp_apple[6]
lp_apple = [apple_copy]

for i in range (6, 0, -1):
    gaussian_extended = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)




#Generate Gaussian Pyramid For Orange
orange_copy =orange.copy()
gp_orange = [orange_copy]

for i in range(6,12):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)
    cv.imshow(str(i), orange_copy)



cv.imshow('apple', apple)
cv.imshow('orange', orange)
cv.imshow('apple_orange', apple_orange)

print(apple.shape)
print(orange.shape)

cv.waitKey(0)
cv.destroyAllWindows()