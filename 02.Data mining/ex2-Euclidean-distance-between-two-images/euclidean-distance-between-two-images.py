#!/usr/bin/env python
# coding: utf-8

# In[14]:


# importing libraries
import numpy as np
import math
import matplotlib.image as img


# In[15]:


# two images to calculate the distance between them
# imgread for transform image tu vector
testImage = img.imread("img-1.png")
testImage2 = img.imread("img-2.png")


# In[16]:


# the image dimensions
# in this example 32*32 it's the pixel number of height and width of the image
# 3 is the main color number (RGB) example: [0,0,0] is [0 red, 0 green and 0 blue] -> so this pixel is black
testImage.shape


# In[17]:


# Euclidean distance using the numpy library
print('Euclidean distance:', np.linalg.norm(testImage - testImage2))


# In[18]:


# Euclidean distance without library
def calculdist() :
    pixels = testImage.shape[0] * testImage.shape[1] * testImage.shape[2]
    distance = 0
    for i in range(0, testImage.shape[0]):
        for j in range(0, testImage.shape[1]):
            for k in range(0, testImage.shape[2]):
                distance += (testImage[i][j][k] - testImage2[i][j][k])**2
    #  if the return is 0, then these are the same images
    return {"distance" : distance, "sqrt distance": math.sqrt(distance), "percentage": distance/pixels } 

print(calculdist())
            

