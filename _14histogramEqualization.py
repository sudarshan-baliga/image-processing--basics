# it is uniformaly distrubuting the histogram to increase the cotrast
# https://en.wikipedia.org/wiki/Histogram_equalization
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("selfie.jpg",0)
equ = cv2.equalizeHist(img)
# cv2.imshow("img", equ)
plt.subplot(121),plt.imshow(img, cmap = "gray"),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(equ, cmap = "gray"),plt.title('equlized')
plt.xticks([]), plt.yticks([])

plt.show()