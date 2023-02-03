"""
@author: SANKET CHOUDHARY
"""

from skimage import color, io
img= io.imread(r'.\img\guy.jpg')
img1= color.gray2rgb(img)
io.imshow()