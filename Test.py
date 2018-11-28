import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("http://10.88.206.32:4747/")
cap = cv2.VideoCapture("http://10.88.206.32:4747/mjpegfeed?640x480")

while(True):
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    _, frame = cap.read()

    cv2.imshow('frame', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == ord("q"):
        break
        

cv2.destroyAllWindows()
cap.release()