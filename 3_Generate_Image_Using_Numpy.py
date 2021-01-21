import numpy as np
import cv2

img = np.zeros([512,512,3],np.uint8) #blackscreen
# img = np.ones([512,512,3]) #whitescreen


cv2.line(img, (0,0), (255,255), (68,105,54), 10) #54, 105, 68
cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 10) #54, 105, 68



cv2.rectangle(img, (384,0), (510,128),(0,0,255), 5)
cv2.rectangle(img, (250,0), (350,128),(0,255,0), -1) #kalo thickness = -1 jadi ngefill warna


cv2.circle(img, (447,63), 63, (255,0,0), -1 )


font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 5, cv2.LINE_AA)



cv2.imshow('Screen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()