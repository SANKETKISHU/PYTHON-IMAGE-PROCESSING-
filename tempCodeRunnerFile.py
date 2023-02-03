#Downscale
"""
@author: SANKET CHOUDHARY
"""
import numpy as np
import cv2 as cv
img= cv.imread('.//img//tiger.jpeg')
cv.imgshow('original', img)
img_half = cv.resize(img,(0,0),fx=0.5, fy=0.5)
cv.imshow('Half_image', img_half)
cv.waitkey(0)
cv.destroyAllWindows()
