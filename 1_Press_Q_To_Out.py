'''Jadi harus mencet q doang biar bisa keluar dari nampilin gambar 
selain itu gabisa'''


import cv2

while (True):
    img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 0)
    cv2.imshow('gambar frame', img)
    k = cv2.waitKey()

    if k == ord('q'):
        cv2.destroyAllWindows()
        break