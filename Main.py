#Main.py
import numpy as np
import cv2
import colorsys

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    _, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width = frame.shape[:2]
    # frame = cv2.resize(frame,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
    # Display the resulting frame
    # cv2.imshow('grayframe',gray)
    # print(frame[0, 0])



    editablePhoto = np.zeros((width,height,3),'float')
    hsvArray=np.zeros((width,height,3),'float')
                
    for i in range(0,width):
        for j in range(0,height):
            for k in range(0,3):
                editablePhoto[i,j,k] = frame[i,j][k]
                editablePhoto[i,j,k] = ((editablePhoto[i,j,k])/255)
            rNew=editablePhoto[i,j,0]
            gNew=editablePhoto[i,j,1]
            bNew=editablePhoto[i,j,2]

            tempArray=np.zeros((3),'float')

            for k in range(0,3):
                hsvArray[i,j,k]=colorsys.rgb_to_hsv(editablePhoto[i,j,0],editablePhoto[i,j,1],editablePhoto[i,j,2])[k]

            print(gNew)
            greenRatio = 0 if gNew == 0 else (hsvArray[i,j,0] - (60/360))/gNew
            blueRange = greenRatio*bNew
            hsvArray[i,j,0] = 0.5 + blueRange

            tempArray=np.zeros((3),'float')
            for k in range(0,3):
                tempArray[k]=hsvArray[i,j,k]
            tempArray.tolist()
            tempArray = (colorsys.hsv_to_rgb(tempArray[0],tempArray[1],tempArray[2]))

            for k in range(0,3):
                editablePhoto[i,j, k] = tempArray[k]*255



    cv2.imshow('frame',editablePhoto)
    # cv2.imshow('a',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
#640 by 480