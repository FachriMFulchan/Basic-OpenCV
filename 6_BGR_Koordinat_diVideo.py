import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(frame, strXY, (x,y), font, 0.5, (0,255,0), 1, cv2.LINE_AA)
        cv2.imshow('video', frame)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = frame[y,x,0]
        green = frame[y,x,1]
        red = frame[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(frame, strBGR, (x,y), font, 0.5, (255,255,255), 1)
        cv2.imshow('video', frame)


while True:
    ret, frame = cap.read()

    cv2.imshow('video', frame)
    cv2.setMouseCallback('video', click_event)

    if cv2.waitKey(1000) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()