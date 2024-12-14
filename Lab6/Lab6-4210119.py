#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
from skimage.io import imread
import numpy as np
from sklearn.cluster import KMeans

original_image = imread('1.jpg')


# In[20]:


#Threshold 
threshold_value = 95
segmented_image = original_image > threshold_value

segmented_image_uint8 = (segmented_image * 255).astype(np.uint8)

#Display the images
fig, axes = plt.subplots(1, 2, figsize=(8, 8))
axes[0].imshow(original_image, cmap='gray')
axes[0].axis('off')
axes[0].set_title('Original Image')
axes[1].imshow(segmented_image_uint8, cmap='gray')
axes[1].axis('off')
axes[1].set_title('Segmented Image (Binary Thresholding)')
plt.show()


# In[31]:


#K-means
pixels = original_image.reshape(-1, 1)

n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(pixels)

segmented_pixels = kmeans.cluster_centers_[kmeans.labels_].reshape(original_image.shape)

# Display the images
fig, axes = plt.subplots(1, 2, figsize=(8, 8))
axes[0].imshow(original_image, cmap='gray')
axes[0].axis('off')
axes[0].set_title('Original Image')
axes[1].imshow(segmented_pixels, cmap='gray')
axes[1].axis('off')
axes[1].set_title('Segmented Image (K-means)')
plt.show()


# In[ ]:





# In[ ]:




