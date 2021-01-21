''' Ketika fotonya ditampilin
ada dua pilihan, 
mencet escape lalu keluar aja
atau mencet save yang akan mensave si gambarnya'''


import cv2
img = cv2.imread('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena.jpg', 0)
cv2.imshow('Gambar Grayscale', img)
print ('Press ESC to Out\nOr \nPress S to save the picture')

k = cv2.waitKey() & 0xFF

if k == 27:
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('D:/A LEARN/Image Processing/Program Youtube/Gambar/lena_grayscale.PNG', img)
    cv2.destroyAllWindows()



