import cv2
import numpy as np

img = cv2.imread('logo.png',0)
retval, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) #to make it as only 1's and zeros
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel, iterations = 1)
dilation = cv2.dilate(img,kernel, iterations = 1)
cv2.namedWindow("dilation")
cv2.namedWindow("erosion")
cv2.namedWindow("img")
cv2.imshow("img", img)
cv2.imshow("dilation",dilation)
cv2.imshow("erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()