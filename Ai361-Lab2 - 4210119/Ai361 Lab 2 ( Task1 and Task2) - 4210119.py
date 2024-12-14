#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install scikit-image


# In[9]:


from skimage import data, io
from skimage.util import crop
import imageio.v3 as iio
import matplotlib.pyplot as plt


# In[39]:


image = iio.imread(uri="image.jpg")
plt.imshow(image)


# In[148]:


cropped_image = image[150:, 0:100]
plt.imshow(cropped_image)


# In[154]:


cropped_image2 = image[0:200:, 0:100]
red= cropped_image2[0:200, 0:100, 0]
io.imshow(red)


# In[156]:


green= cropped_image2[0:200, 0:100, 1]
io.imshow(green)


# In[158]:


blue= cropped_image2[0:200, 0:100, 2]
io.imshow(blue)


# In[164]:


from skimage import exposure
import imageio.v3 as iio
import matplotlib.pyplot as plt
dog= iio.imread(uri='DogPic.jpg')
plt.imshow(dog)


# In[174]:


gamma= exposure.adjust_gamma(dog, 0.30)
plt.imshow(gamma)


# In[ ]:




