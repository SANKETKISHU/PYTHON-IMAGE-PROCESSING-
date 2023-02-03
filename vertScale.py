"""
@author: SANKET CHOUDHARY
"""
# from matplotlib.hatch import HorizontalHatch
# import numpy as np

import cv2
img= cv2.imread(r".\img\messi.jpeg")
cv2.imshow("Original Image",img)
new_width= 900
print(type(img))
print(img.shape)
dim_size= (new_width, img.shape[1])  # creating a tuple
# dim_size= (new_width,900) # study purpose
vertical_scale= cv2.resize(img, dim_size)
cv2.imshow("Vertical Scaled image", vertical_scale)
cv2.waitKey(0)
cv2.destroyAllWindows()
