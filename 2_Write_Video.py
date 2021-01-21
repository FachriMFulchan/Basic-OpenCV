import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #bisa juga ('X','V','I','D')
out = cv2.VideoWriter('D:/A LEARN/Image Processing/Program Youtube/Gambar/outputmp4.mp4', fourcc, 20.0, (640,480))


while True:
    ret, frame = cap.read()

    if ret == True :
        
        #output warna
        out.write (frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #output grayscale
        # out.write (gray)
        #gabisa ternyata gais
       
        cv2.imshow('video grayscale', gray)

        if cv2.waitKey(1) == ord('q'):
            break
    else :
        break

cap.release()
out.release()
cv2.destroyAllWindows()