# first convert image to hsv fomat
#then  threshold the HSV image to get only blue colors (this will have 0(black color for none blue colrs))
#do bitwise and to get show only blue colors
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
# for calculating hsv
# >>> green = np.uint8([[[0,255,0 ]]])
# >>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# >>> print hsv_green
# [[[ 60 255 255]]]