"""
@author: SANKET CHOUDHARY
"""

import numpy as np 
from skimage import data 
import matplotlib.pyplot as plt

image = data.camera()
mask = image<20
image[mask] = 255
plt.imshow(image, cmap='gray')

