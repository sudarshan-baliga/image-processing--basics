import numpy as np
import cv2

im = cv2.imread('selfie.jpg')
print(im.shape[::-1])
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
thresh =cv2.adaptiveThreshold(imgray, 150, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) #(img, max)

# thresh = cv2.bitwise_not(thresh)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# in second arguement use cv2.RETR_TREE to get only bounry contours
img = cv2.drawContours(im, contours, -1, (0,255,0), 3) #image, list of countour(numpy array of (x, y)), which index(-1 for all), color, stroke
cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()