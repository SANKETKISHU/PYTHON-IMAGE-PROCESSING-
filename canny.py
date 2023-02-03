# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:28:17 2022

@author: SANKET CHOUDHARY
"""

import matplotlib.pyplot as plt
from skimage import data, feature
image = data.horse()
edges = feature.canny(image, sigma=3)
plt.imshow(edges, cmap='gray')                                         