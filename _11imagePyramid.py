# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_pyramids/py_pyramids.html#py-pyramids

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('selfie.jpg', 0)
lower_reso = img
for i in range(4):
    lower_reso = cv2.pyrDown(lower_reso)
    plt.subplot(1,4,i + 1),plt.imshow(lower_reso,cmap = 'gray')
    plt.title("pyramid level " + str(i + 1) + " "), plt.xticks([]), plt.yticks([])
plt.show()

# can be used for image blendign (looks a bit complex)