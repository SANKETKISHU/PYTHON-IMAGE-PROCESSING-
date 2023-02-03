"""
@author: SANKET CHOUDHARY
"""


import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'./img/jutsu.jpg')
img1 = cv2.imread(r'./img/jutsu.jpg')
#image concatenation
# images = np.concatenate((img,img1), axis=1)
# cv2.imshow("images",images)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

grey_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey_img1= cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
hist = cv2.calHist(grey_img, [0], None, [256], [0,256])
hist1 = cv2.calcHist(grey_img1, [0], None, [256], [0,256])
plt.subplot(1,2,1)
plt.title("image 1")
plt.xlabel("bins")
plt.ylabel("No. of pixels")
plt.plot(hist)
plt.subplot(1,2,2)
plt.title("Image 2")
plt.xlabel("bins")
plt.ylabel("No. of pixels")
plt.plot(hist1)
plt.show()



