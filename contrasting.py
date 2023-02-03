"""
Created on Wed Aug 24 09:28:17 2022

@author: SANKET CHOUDHARY
"""


from PIL import Image, ImageEnhance
import numpy as np
img = Image.open(r'./img/jutsu.jpg')
img.show('original')
layer1 = ImageEnhance.Contrast(img)
layer1.enhance(10).show("10% More Contrast")
