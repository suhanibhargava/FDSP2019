# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:37:40 2019

@author: Dell
"""

import imageio
import os

path = "D:\Training@FORSK2019\Day10\pics"
image_folder = os.fsencode(path)

filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( '.jpg' ):
        filenames.append(filename)

filenames.sort() # this iteration technique has no built in order, so sort the frames

images = list(map(lambda filename: imageio.imread(filename), filenames))

imageio.mimsave(os.path.join('movie1.gif'), images, duration = 1.0)