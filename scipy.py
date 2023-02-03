"""
@author: SANKET CHOUDHARY
"""
import matplotlib.pyplot as plt
from scipy import misc, ndimage
face = misc.face()
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred_image = ndimage.gaussian_filter(face, sigma=5)
plt.imshow(blurred_face)