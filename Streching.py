#Streching
"""
@author: SANKET CHOUDHARY
"""
import numpy as np
import cv2 as cv
img = cv.imread('.//img//tiger.jpeg')
cv.imshow('original', img)
# cv.waitKey(0)
img_stretched= cv.resize(img,(400, 400))
cv.imshow("Stretched", img_stretched)
cv.waitKey(0)
cv.destroyAllWindows()