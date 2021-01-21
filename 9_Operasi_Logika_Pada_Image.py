import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
cv2.rectangle(img1, (250,0), (500,250), (255,255,255), -1)  #ini formatnya beda ya dari baris, kolom

img2 = np.zeros((250,500,3), np.uint8)
cv2.rectangle(img2, (200,0), (300, 100), (255,255,255), -1)

bitAnd = cv2.bitwise_and(img1, img2) #AND
bitOr = cv2.bitwise_or(img1, img2) #OR
# bitXor = cv2.bitwise_xor(img1, img2) #XOR
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('And', bitAnd)
cv2.imshow('Or', bitOr)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)
cv2.waitKey()
cv2.destroyAllWindows()