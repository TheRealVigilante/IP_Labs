from skimage import io
import matplotlib.pyplot as plt

defect = io.imread("KSA1.jpg")
plt.imshow(defect)
plt.show()