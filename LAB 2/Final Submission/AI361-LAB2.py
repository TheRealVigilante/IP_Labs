#!/usr/bin/env python
# coding: utf-8

# In[73]:


from skimage import io,exposure,color
import numpy as np


# In[75]:


image = io.imread("image.jpg")


# In[77]:


image1_shuttle = image[150:, 0:100]
io.imshow(image1_shuttle)
io.show()


# In[116]:


red = image.copy()[0:200,150:300,0]

green = image.copy()[0:200,150:300,1]

blue = image.copy()[0:200,150:300,2]


# In[120]:


io.imshow(red)
io.show()


# In[83]:


io.imshow(green)
io.show()


# In[85]:


io.imshow(blue)
io.show()


# ### Red channel is 0
# ### Green channel is 1
# ### Blue channel is 2

# ### Extra Challenge

# In[126]:


image2 = image.copy()
white_threshold = 220
black_threshold = 35
for i in range(image2.shape[0]):
    for j in range(image2.shape[1]):
        r,g,b = image2[i,j]
        if r>=white_threshold and g>=white_threshold and b >=white_threshold:
            image2[i,j,0] = 255
            image2[i,j,1]=0
            image2[i,j,2]=0

        if r<=black_threshold and g<=black_threshold and b<=black_threshold:
            image2[i,j,0]=0
            image2[i,j,1]=0
            image2[i,j,2]=255
io.imshow(image2)
io.show()


# ### TASK 2

# In[33]:


from skimage import exposure


# In[39]:


dog = io.imread("Dog.png")
gamma = float(input("Insert the level of brightness you want (brighter<1, same = 1, darker >1):"))
new = exposure.adjust_gamma(dog, gamma)
io.imshow(new)
io.show()


# In[ ]:




