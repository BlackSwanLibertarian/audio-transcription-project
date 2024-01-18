# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:27:28 2023

@author: raamc
"""

from PIL import Image
import pytesseract
from IPython.display import display

# Load the image from file
img_path = '/mnt/data/image.png'
img = Image.open(img_path)

# Since we cannot use OCR here and we need to manually inspect the image, let's display it.
display(img)
