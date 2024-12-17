from skimage import io,exposure,color
import matplotlib.pyplot as plt
import numpy as np


image = io.imread("image.jpg")

#PART 1
image1_shuttle = image[150:, 0:100]

# plt.imshow(image1_shuttle)
# plt.show()

red = image.copy()[0:200,150:300,0]

green = image.copy()[0:200,150:300,1]

blue = image.copy()[0:200,150:300,2]

io.imshow(red)
io.imshow(green)
io.imshow(blue)

io.show()

#Red channel is 0, Green channel is 1,Blue channel is 2
