import cv2

cap = cv2.VideoCapture(0)
print (cap.isOpened())

while True :
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video frame grayscale', gray)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



#cap.isOpened()
#bisa juga dipake buat kondisi while

#while cap.isOpened()
#jadi kalo False dibawahnya gaakan dieksekusi
