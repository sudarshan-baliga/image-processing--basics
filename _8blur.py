# https://www.youtube.com/watch?v=C_zFhWdM4ic

# 2D Convolution ( Image Filtering ) just averaging the pixels under the kernel
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel) # -1 ddepth (destination image depth) -1 means same as original
 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

# same as above just averaging
img = cv2.imread('logo.png')

blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('2Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('2Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#for gausian only kernel is different https://www.youtube.com/watch?v=C_zFhWdM4ic
# . We also should specify the standard deviation in X and Y direction, sigmaX and sigmaY respectively.
# blur = cv2.GaussianBlur(img,(5,5),0) 

#for median median pixel is choosen whichis under the kernel
# median = cv2.medianBlur(img,5)


# Bilateral filter also takes a gaussian filter in space, but one more gaussian filter which is a function of pixel difference.
#  Gaussian function of space make sure only nearby pixels are considered for blurring while gaussian function of intensity 
# difference make sure only those pixels with similar intensity to central pixel is considered for blurring.
# So it preserves the edges since pixels at edges will have large intensity variation.
# Below samples shows use bilateral filter (For details on arguments, visit docs).

# blur = cv2.bilateralFilter(img,9,75,75)
# cv2.bilateralFilter() is highly effective in noise removal while keeping edges sharp