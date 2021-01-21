import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 1)
img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#matplotlib ngebaca dan menampilkan dalam fromat RGB

cv.imshow('image', img)

plt.imshow(img2, 'gray')
plt.xticks([])  #ngilangin sumbu x dan y nyaa
plt.yticks([])

plt.show()

cv.waitKey()
cv.destroyAllWindows()