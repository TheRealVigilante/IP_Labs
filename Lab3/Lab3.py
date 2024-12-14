#!/usr/bin/env python
# coding: utf-8

# In[187]:


from skimage import io, filters, morphology
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

pic= io.imread('Picture1.jpg')

if pic.shape[2]==4:
    pic= pic[:,:,:3]

pic_grayscale= rgb2gray(pic)
remove_noise= filters.median(pic_grayscale, morphology.disk(5))

io.imshow(remove_noise)
plt.axis('off')




# In[ ]:




