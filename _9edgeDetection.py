# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_gradients/py_gradients.html#gradients
# sobel:
# https://www.youtube.com/watch?v=iendD-Iqoog

# Laplacian Derivatives:
# https://www.youtube.com/watch?v=zQKNVept4bU
# https://www.youtube.com/watch?v=1b3Sr2MGLFg

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo.png',0)


# cv_64f is used to make double data type as destination
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)


plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

# to get better output in sobel run gausian filter on greyscale image then apply sobel
# for clear output final sobel output image should be sqrt(x ^2 + y ^ 2) not sure how to do that for now