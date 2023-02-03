"""
@author: SANKET CHOUDHARY
"""

import cv2 
img = cv2.imread(r'C:\Users\user\OneDrive - Amity University\BCA 5th Sem\ImgProcessing\ImgProcessingPrac\img\cycling.jpg')

# Zooming it by 10x
nearest = cv2.resize(img, (250,250), interpolation=cv2.INTER_NEAREST)
linear = cv2.resize(img, (250,250), interpolation=cv2.INTER_LINEAR)
cubic = cv2.resize(img, (250,250), interpolation=cv2.INTER_CUBIC)

cv2.imshow('Nearest', nearest)
cv2.imshow('Linear', linear)
cv2.imshow('Cubic', cubic)
cv2.waitKey(3000)
cv2.destroyAllwindows()