#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install ipympl')


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import ipympl
import imageio.v3 as iio
import skimage


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


eight = iio.imread(uri="eight.tif")
plt.imshow(eight)


# In[5]:


print(eight.shape)
print(eight)


# In[6]:


zero = iio.imread(uri="eight.tif")
zero[3,0]= 1
zero[1,2]= 1



"""
The follwing line of code creates a new figure for imshow to use in displaying our output. Without it, plt.imshow() would overwrite our previous image in the cell above
"""
fig, ax = plt.subplots()
plt.imshow(zero)
print(zero)


# In[7]:


# make a copy of eight
three_colours = iio.imread(uri="eight.tif")

# multiply the whole matrix by 128
three_colours = three_colours * 128

# set the middle row (index 2) to the value of 255.,
# so you end up with the values 0., 128., and 255.
three_colours[2,:] = 255.
fig, ax = plt.subplots()
plt.imshow(three_colours)
print(three_colours)


# In[8]:


fig, ax = plt.subplots()
plt.imshow(three_colours,cmap=plt.cm.gray)


# In[9]:


# set the random seed so we all get the same matrix
pseudorandomizer = np.random.RandomState(2021)
# create a 4 × 4 checkerboard of random colours
checkerboard = pseudorandomizer.randint(0, 255, size=(4, 4, 3))
# restore the default map as you show the image
fig, ax = plt.subplots()
plt.imshow(checkerboard)
# display the arrays
print(checkerboard)

