import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/apple.jpg', 1)
layer = img.copy()
gp = [layer]


for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow(str(i), layer)


#upper level gaussian
layer = gp[6]


for i in range(6, 0, -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)


cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()