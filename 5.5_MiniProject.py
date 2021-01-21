import cv2
import datetime

cap = cv2.VideoCapture(0)

cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.get(4))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width : '+ str(cap.get(3)) + ' Height : ' + str(cap.get(4))
        datet = str(datetime.datetime.now())

        cv2.putText(frame, text, (10,50), font, 1, (0,255,255), 1, cv2.LINE_AA)
        cv2.putText(frame, datet, (220,460), font, 1, (0,0,255), 1, cv2.LINE_AA)

        cv2.rectangle(frame, (180,80), (460,380), (4,196, 23), 2, cv2.LINE_AA)
        

        cv2.imshow('Live Video', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    
    else:
        break
cap.release()
cv2.destroyAllWindows()
    
