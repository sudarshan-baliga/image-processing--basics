# make everthing either 1 or zero (can be plane red, green or blue also if image is colored)

import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) #(img, minval, maxval,method ) assuming 12 as white and 255 as black 

retval2, grayThreshold = cv2.threshold(imgGray, 10, 255, cv2.THRESH_BINARY)
adp = cv2.adaptiveThreshold(imgGray, 150, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) #(img, max)
# in the above method(adaptive) we can have two methods
# ADAPTIVE_THRESH_MEAN_C − threshold value is the mean of neighborhood area.
# ADAPTIVE_THRESH_GAUSSIAN_C − threshold value is the weighted sum of neighborhood values where weights are a Gaussian window.
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow("gray", grayThreshold)
cv2.imshow("adpative", adp)
cv2.waitKey(0)
cv2.destroyAllWindows()