import cv2

cap = cv2.VideoCapture(0)
print (cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print (cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(3, 1208)
cap.set(4, 720)

print (cap.get(3))
print (cap.get(4))


while (True):
    ret, frame = cap.read()

    cv2.imshow('video frame', frame)

    if cv2.waitKey(1)  == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()