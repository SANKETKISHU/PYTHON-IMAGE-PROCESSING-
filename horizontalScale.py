"""
@author: SANKET CHOUDHARY
"""
import cv2
img= cv2.imread(r".\img\messi.jpeg")
cv2.imshow("Original Image",img)
new_width= 900
print(type(img))
print(img.shape)
dim_size= (img.shape[1], new_width)  # creating a tuple
# dim_size= (new_width,900) # study purpose
horizontal_scale= cv2.resize(img, dim_size)
cv2.imshow("Vertical Scaled image", horizontal_scale)
cv2.waitKey(0)
cv2.destroyAllWindows()