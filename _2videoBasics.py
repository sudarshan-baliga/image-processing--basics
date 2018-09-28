import numpy as np
import cv2

#start the camera recording
cap = cv2.VideoCapture(0)

while(True):
    # get the frame 
    ret, frame = cap.read()

    # convert it to grayscale (not required just to make the process faster since each pixel 
    # can have only 255 possible value in grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #pass 1 for colorful image

    # Display the resulting frame
    cv2.imshow('frame',gray) 
    # press q to exit
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()