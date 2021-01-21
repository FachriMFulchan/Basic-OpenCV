import cv2

cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()
    
    a = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    b = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print ('Width : {}, Height : {}'.format(a,b))    

    cv2.imshow('video stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()