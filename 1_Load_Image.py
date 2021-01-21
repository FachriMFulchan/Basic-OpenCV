import cv2
img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 3)
print (img)
cv2.imshow('image', img)
cv2.waitKey()
#cv2.waitKey(0) sama aja kaya ini

cv2.destroyAllWindows()
cv2.imwrite('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena_grayscale.PNG', img)


