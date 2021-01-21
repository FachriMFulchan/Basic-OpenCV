import cv2
import numpy as np

'''Untuk mengetahui apa apa saja yang
bisa dilakukan oleh mouse, bisa dilihat
pada EVENT di dir cv2,
gini nih cara liatnya '''


#Cara cepet tapi susah
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print (events)


# #cara lama cuma gampang
# for i in dir(cv2):
#     if 'EVENT' in i:
#         print (i)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, 1, (255,255,0), 2, cv2.LINE_AA)
        cv2.imshow('image', img)



img = np.zeros((512,512, 3), np.uint8)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''SetMouseCallback tuh
default nya langsung ngasih 5 parameter otomatis yaitu
event, x, y, flags, param
udah gabisa diganggu gugat itumaa
'''

