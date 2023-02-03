"""
@author: SANKET CHOUDHARY
"""

import matplotlib.pyplot as plt
from skimage import data, filters
img= (r".img\guy.jpg")
egdes= filters.sobel(img)
plt.imshow(egdes, cmap='gray')