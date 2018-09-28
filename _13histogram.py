# it is intensity of colors shown in graph
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('selfie.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    # ([image], [channel], mask, histsize, range)
    # channel = 0 for grey , for color [0],[1],[2] for r, g, b respectively
    #mask is to find histogram in only required part
    #histsize is bin count, if we want bin for each pixel we pass [256]
    #range of values in x is range
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()