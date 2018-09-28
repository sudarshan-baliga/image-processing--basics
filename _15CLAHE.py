# cv2.equalizeHist method equalizes considering global contrast this will give 
#inadequent output
# CLAHE (Contrast Limited Adaptive Histogram Equalization)
#  In this, image is divided into small blocks called “tiles” 
#  (tileSize is 8x8 by default in OpenCV). 
#  Then each of these blocks are histogram equalized as usual.
# https://en.wikipedia.org/wiki/Histogram_equalization refer this for working
import numpy as np
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('selfie.jpg',0)
normalHista = cv2.equalizeHist(img)
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)


plt.subplot(121), plt.imshow(img, cmap = "gray")
plt.title("normalequalization"), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cl1, cmap = "gray")
plt.title("clahe"), plt.xticks([]), plt.yticks([])

plt.show()
