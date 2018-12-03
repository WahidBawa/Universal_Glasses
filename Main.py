#Main.py
import numpy as np
import cv2
import colorsys

# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("http://10.88.206.32:8080/video")
# cap = cv2.VideoCapture("http://10.88.206.32:4747/mjpegfeed?640x480")

#MOTO G3
# cap = cv2.VideoCapture("http://192.168.0.75:8080/video")
# cap = cv2.VideoCapture("http://192.168.0.75:4747/mjpegfeed?640x480")
cap = cv2.VideoCapture("http://10.42.0.248:4747/mjpegfeed?640x480")
while(True):
    _, frame = cap.read()
    width, height = 100, 25
    editablePhoto = np.zeros((width,height,3),'float')
    for i in range(0, 100):
        for j in range(0, 25):
            for k in range(0, 3):
                # if k == 0:
                #     editablePhoto[i, j][k] *= 1.15
                # if k == 1:
                #     editablePhoto[i, j][k] *= 2.4546
                if k == 2:
                    editablePhoto[i, j][k] = frame[i, j][k]
                    editablePhoto[i, j][k] = editablePhoto[i,j,k]/255
                    editablePhoto[i, j][k] *= .56465
                    frame[i, j][k] = editablePhoto[i, j][k];
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
