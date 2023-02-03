"""
@author: SANKET CHOUDHARY
"""

from PIL import Image
img = Image.open(r".\img\cycling.jpg")
img.show("Original")
 
angle = 180
output = img.rotate(angle)
output.show()
 
angle1 = 90
output = img.rotate(angle1)
output.show()
