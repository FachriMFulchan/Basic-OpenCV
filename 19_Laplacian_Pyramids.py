'''Jadi Laplacian Pyramids tuh
nge Substract antara Image yang udah di PyrUp (blur)
dan yang di PyrDown
Dengan resolusi frame yang sama
Jadilah kaya edge gitu
Bahasa bagusnya ada di word'''


import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 1)

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    # cv.imshow(str(i), layer)


#Upper Level Gaussian
layer = gp[6]
cv.imshow('Upper Level Gaussian Pyramid', layer)
lp = [layer]


for i in range(6, 0, -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)



cv.imshow('Image asli', img)
cv.waitKey(0)
cv.destroyAllWindows()