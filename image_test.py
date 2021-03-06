import numpy as np
import cv2
import colorsys

# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("http://10.88.206.32:8080/video")
# cap = cv2.VideoCapture("http://10.88.206.32:4747/mjpegfeed?640x480")

# cap = cv2.VideoCapture("http://192.168.0.75:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://192.168.0.75:4747/mjpegfeed?320x240")
# cap = cv2.VideoCapture("http://10.42.0.248:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://10.42.0.248:4747/mjpegfeed?320x240")

path = input("Enter in an image: ")
while(True):
    # _, frame = cap.read()
    frame = cv2.imread("/home/wahid/Documents/GitHub/Universal_Glasses/normal_images/" + path)
    cv2.imshow('img1', frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('q'): #save on pressing 'q' 
        cv2.imwrite('results/normal.png', frame)
        height, width = frame.shape[:2]
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

                if gNew > 0:
                    greenRatio = (hsvArray[i,j,0] - (60/360))/gNew
                    blueRange = greenRatio*bNew
                    hsvArray[i,j,0] = 0.5 + blueRange

                tempArray=np.zeros((3),'float')
                for k in range(0,3):
                    tempArray[k]=hsvArray[i,j,k]
                tempArray.tolist()
                tempArray = (colorsys.hsv_to_rgb(tempArray[0],tempArray[1],tempArray[2]))

                for k in range(0,3):
                    editablePhoto[i,j, k] = tempArray[k]*255
                frame[i, j, k] = editablePhoto[i, j, k]
        NormalPhoto = editablePhoto
        for i in range(0,width):
            for j in range(0,height):
                for k in range(0,3):
                    frame[i,j,k] = NormalPhoto[i, j, k]
        cv2.imwrite('results/correct.png',frame)
        cv2.destroyAllWindows()
        break

    # cv2.imshow('frame', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
# When everything done, release the capture
# cap.release()
cv2.destroyAllWindows()
#NMJ3KR2W
#inputIm = Image.open(user_choice.input)