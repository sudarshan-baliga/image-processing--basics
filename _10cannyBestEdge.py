# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_canny/py_canny.html#canny
#combines sobel(both direction), gausian + some tweaks to get best edges(like finding the local maximum,
#  finding sure edges which are above threshold values etc)

import cv2
import numpy as np  
from matplotlib import pyplot as plt


img = cv2.imread("selfie.jpg", 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),
plt.subplot(122), plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()