import numpy as np
import cv2

logo = cv2.imread("logo.png")
img = cv2.imread("selfie.jpg")

rows,cols,channels = logo.shape
roi = img[0:rows, 0:cols ]


graylogo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
threshold,mask = cv2.threshold(graylogo, 150, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv2.bitwise_and(logo,logo,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img[0:rows, 0:cols ] = dst

cv2.namedWindow("logo", cv2.WINDOW_NORMAL)
cv2.imshow("logo", mask_inv)
cv2.imshow("selfie", img)
cv2.waitKey(0)
cv2.destroyAllWindows()