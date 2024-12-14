import matplotlib.pyplot as plt
import matplotlib.image as img
import imageio.v3 as iio
import numpy as np


image_path = input("Enter the path of the image: ")
image = img.imread(image_path)
new_image = np.copy(image)
alpha_value = int(input("Enter the transparency level (0 to 255): "))
path= input("enter the path for the new image")

for i in range(new_image.shape[0]):
    for j in range(new_image.shape[1]):
        new_image[i, j, 2] = alpha_value

plt.imshow(new_image)
iio.imwrite(path,new_image)