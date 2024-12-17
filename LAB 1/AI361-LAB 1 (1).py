#!/usr/bin/env python
# coding: utf-8

# In[82]:


pip install ipympl --user


# In[7]:


import numpy as np
import matplotlib.pyplot as plt
import ipympl
import imageio.v3 as iio
import skimage


# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


image = r"C:\Users\4311779\Downloads\eight.tif"


# In[22]:


eight = iio.imread(image)
plt.imshow(eight)


# In[24]:


print(eight.shape)
print(eight)


# In[26]:


zero = iio.imread(uri="eight.tif")
zero[2,1]= 1.0
"""
The follwing line of code creates a new figure for imshow to use in displaying our output. Without it, plt.imshow() would overwrite our previous image in the cell above
"""
fig, ax = plt.subplots()
plt.imshow(zero)
print(zero)


# In[28]:


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


# In[30]:


fig, ax = plt.subplots()
plt.imshow(three_colours,cmap=plt.cm.gray)


# In[32]:


# set the random seed so we all get the same matrix
pseudorandomizer = np.random.RandomState(2021)
# create a 4 × 4 checkerboard of random colours
checkerboard = pseudorandomizer.randint(0, 255, size=(4, 4, 3))
# restore the default map as you show the image
fig, ax = plt.subplots()
plt.imshow(checkerboard)
# display the arrays
print(checkerboard)


# 

# In[34]:


five = iio.imread(uri="eight.tif")
five[1,2]=1.0
five[3,0]=1.0
print(five)
plt.imshow(five)


# #Exercise 2
# Loading an image
# 
# changing the transparency 
# 
# displaying the output

# In[124]:


InputPath = input("Enter the Path of the original image")
Modification = int(input("Enter the desired change level: (0-255)"))
OutputPath = input("Enter the Path of the modified image")

#InputPath = "puppy.jpg"
Img = iio.imread(InputPath)
#print(Img.shape)

for i in range(Img.shape[0]):
    for j in range(Img.shape[1]):
        #Img[i,j,2] = 255
        Img[i,j,2] = Modification

plt.imshow(Img)
iio.imwrite(OutputPath, Img)


# In[ ]:




