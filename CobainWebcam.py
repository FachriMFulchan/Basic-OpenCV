import cv2 as cv
import time

vs = cv.VideoCapture(0)
vs.set(3, 1280)
vs.set(4, 480)
vs.set(cv.CAP_PROP_BUFFERSIZE, 3);
vs.set(cv.CAP_PROP_FPS, 30);
vs.set(cv.CAP_PROP_POS_FRAMES , 3);
time.sleep(2.0)


while True :
    _, frame = vs.read()
    cv.imshow ('frame', frame)

    k = cv.waitKey(1)
    if k == ord('q'):
        break

vs.release()
cv.destroyAllWindows()