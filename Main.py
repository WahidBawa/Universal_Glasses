#Main.py
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    _, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    # cv2.imshow('grayframe',gray)
    # print(frame[0, 0])z
    for f in range(100):
        for i in range(100):
            for n in range(3):
                frame[f, i][n] = 0 
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
#640 by 480