import numpy as np
import cv2 

img = cv2.imread("selfie.jpg", 0)

cv2.namedWindow('image', cv2.WINDOW_NORMAL) #we can resize if we create the window before adding image
cv2.rectangle(img,(3846,0),(510,128),(0,255,0),1) #(img, topleft, bottom right, color, stroke)
# img[10:100, 400:3000] = img[410:500, 400:3000] #we cut change a part of image like this
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()