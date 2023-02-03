#Upscaling
"""
@author: SANKET CHOUDHARY
"""
import cv2
img = cv2.imread('.//img//forest.jpg')
cv2.imshow("original",img)
img_up= cv2.resize(img,(0,0),fx=2.5,fy=2.5)
cv2.imshow("Upscaled image",img_up)
cv2.waitKey(0)
cv2.destroyAllWindows()