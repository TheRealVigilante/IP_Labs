from skimage import filters,io
from skimage.segmentation import slic, mark_boundaries
import matplotlib.pyplot as plt

image = io.imread("43.jpg")
print(image.shape)

def plot_comparison(original, processed, title):
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    ax = axes.ravel()

    io.imshow(original, ax=ax[0] , cmap = 'gray')
    ax[0].set_title("Original")

    io.imshow(processed, ax=ax[1], cmap = 'gray')
    ax[1].set_title(title)

    for a in ax:
        a.axis('off')

    io.show()

# date1 = io.imread("43.jpg", as_gray=True)
# date2 = io.imread("428.jpg", as_gray=True)
# date3 = io.imread("444.jpg", as_gray=True)
#
# niblack_threshold1 = filters.threshold_niblack(date1)
# niblack_threshold2 = filters.threshold_niblack(date2)
# niblack_threshold3 = filters.threshold_niblack(date3)
#
# binary_date1 = date1 > niblack_threshold1
# binary_date2 = date2 > niblack_threshold2
# binary_date3 = date3 > niblack_threshold3
#
# # plot_comparison(date1, binary_date1, "Niblack Thresholding")
# # plot_comparison(date2, binary_date2, "Niblack Thresholding")
# # plot_comparison(date3, binary_date3, "Niblack Thresholding")
#
# date1_segments = slic(date1, n_segments=200, compactness=0.02, channel_axis=None)
# date2_segments = slic(date2, n_segments=200, compactness=0.04, channel_axis=None)
# date3_segments = slic(date3, n_segments=250, compactness=0.01, channel_axis=None)

# plot_comparison(date1, mark_boundaries(date1, date1_segments), "SLIC Segmentation")
# plot_comparison(date2, mark_boundaries(date2, date2_segments), "SLIC Segmentation")
# plot_comparison(date3, mark_boundaries(date3, date3_segments), "SLIC Segmentation")