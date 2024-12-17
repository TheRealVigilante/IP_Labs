from skimage import io,exposure
import matplotlib.pyplot as plt

dog = io.imread("Dog.png")
gamma = float(input("Insert the level of brightness you want (brighter<1, same = 1, darker >1):"))
new = exposure.adjust_gamma(dog, gamma)
io.imshow(new)
io.show()