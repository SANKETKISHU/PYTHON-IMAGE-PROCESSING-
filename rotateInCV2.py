"""
@author: SANKET CHOUDHARY
"""

import cv2
img = cv2.imread(r'./img/messi.jpeg')
res90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
res180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("90 degree rotated", res90)
cv2.imshow("180 degree rotateed", res180)
cv2.waitKey(3000)
cv2.destroyAllWindows()