#Downscale
#Author: Akash Sinha
# import numpy as np
import cv2
img= cv2.imread('.//img//messi.jpeg')
cv2.imshow('original', img)
img_half = cv2.resize(img,(0,0),fx=0.5, fy=0.5)
cv2.imshow('Half_image', img_half)
cv2.waitkey(0)
cv2.destroyAllWindows()
