import os
import shutil
import sys
import numpy as np
from PIL import Image

file_extension = ["jpg", "bmp", "png"]
replace_color = [0,0,0,0]

def replaceColor(img, targetColor, newColor):
  data = np.array(img)
  rgb = data[:,:,:3]
  mask = np.all(rgb == targetColor, axis = -1)
  data[mask] = newColor
  return Image.fromarray(data)

def saveRemoveWhiteColor(img,path):
  for i in range(220,256):
    img = replaceColor(img, [i,i,i], replace_color)
    if i==255:
      for ext in file_extension:
        if (path.endswith("."+ext)):
          img.save(path.replace("."+ext,'.png'))
          break

def saveRemoveBlackColor(img,path):
  for i in range(0,5):
    img = replaceColor(img, [i,i,i], replace_color)
    if i==4:
      for ext in file_extension:
        if (path.endswith("."+ext)):
          img.save(path.replace("."+ext,'.png'))
          break

# Remove white colour to transparent program in python

# Prerequisite:
# pip install numpy
# pip install Pillow

# Description
# The sample project provide you an example to remove specfic colours into transparent colour of bmp images.
# Please put images in root directory.

for root, dirss, files in os.walk(".."):
  for filename in files:
    for ext in file_extension:
      if (filename.endswith("."+ext)):
        img = Image.open(filename)
        img = img.convert('RGBA')
        saveRemoveWhiteColor(img, filename.split(".")[0] + "_modified.png")
