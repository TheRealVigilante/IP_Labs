from skimage import io
from skimage.filters import median,rank
from skimage.morphology import diamond,disk,star
from skimage.exposure import adjust_gamma

img = io.imread('image.png', as_gray=True)
noiselessIMG = median(img, disk(3))
noiselessIMG = rank.mean(noiselessIMG,diamond(3))
# noiselessIMG = adjust_gamma(noiselessIMG,0.8)
io.imshow(noiselessIMG)
io.show()

