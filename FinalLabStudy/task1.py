from skimage import exposure, io, img_as_float,color
from skimage.filters import unsharp_mask
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = io.imread('FinalLabStudy/Picture1.jpg')
# plt.imshow(image)
# plt.show()

# Take input from the user
brightness_level = float(input("Enter the brightness adjustment value: "))
contrast_factor = float(input("Enter the contrast scaling value: "))
hue_adjust = int(input("Enter the hue value(by an angle): "))

def adjust_brightness_skimage_rgb(image, brightness_level):
    # Ensure the input image is in float format (range 0.0 to 1.0)
    image = img_as_float(image)

    brightness_level = brightness_level/255.0

    for i in range(3):
        # Apply gamma adjustment to each channel
        image[:, :, i] = image[:, :, i] + brightness_level
    
    # Clip the values to stay within the range [0, 1]
    adjusted_image = np.clip(image, 0, 1)

    return adjusted_image

# Apply gamma adjustment
adjusted_image = adjust_brightness_skimage_rgb(image, brightness_level)
    

def adjust_contrast_rescale(image, contrast_factor, output_range=(0, 255)):
    # Ensure the image is in float format (range 0.0 to 1.0)
    image = img_as_float(image)

    # Initialize the output image
    stretched_image = np.zeros_like(image)

    for i in range(3):
        # Apply contrast scaling to each channel
        stretched_image[:, :, i] = contrast_factor * image[:, :, i]
        
    return stretched_image

stretched_image = adjust_contrast_rescale(image, contrast_factor)

def adjust_hue_skimage_rgb(image, hue_adjust):
    image = color.rgb2hsv(image)

    print(image[..., 0])

    # Adjust the hue by the specified angle
    image[:, :, 0] = image[:, :, 0] + hue_adjust/360.0

    # Convert the image back to RGB format
    adjusted_image = color.hsv2rgb(image)

    return adjusted_image

hued_image = adjust_hue_skimage_rgb(stretched_image, hue_adjust)

sharpened_image = unsharp_mask(hued_image, radius=1, amount=1)


def report():
    print("Brightness adjustment value: ", brightness_level)
    print("Contrast scaling value: ", contrast_factor)
    print("Hue value(by an angle): ", hue_adjust)
    print()
    print("1. Load the image")
    print("2. Take input from the user")
    print("3. Apply brightness adjustment")
    print("4. Apply contrast scaling")
    print("5. Apply hue adjustment")
    print("6. Apply unsharp mask")
    print("7. Display the results")
    print("8. Save the results")
    # Display the results
    fig, axes = plt.subplots(1, 5, figsize=(12, 12))
    ax = axes.ravel()

    ax[0].imshow(image)
    ax[0].set_title("Original Image")
    ax[0].axis('off')

    ax[1].imshow(adjusted_image)
    ax[1].set_title("Brightness Adjustment: " + str(brightness_level))
    ax[1].axis('off')

    ax[2].imshow(stretched_image)
    ax[2].set_title("Contrast Scaling: "+ str(contrast_factor))
    ax[2].axis('off')

    ax[3].imshow(hued_image)
    ax[3].set_title("Hue Adjustment: "+ str(hue_adjust))
    ax[3].axis('off')

    ax[4].imshow(sharpened_image)
    ax[4].set_title("Unsharp Mask")
    ax[4].axis('off')

    #Save the results
    io.imsave('FinalLabStudy/Results/task1_output.jpg', sharpened_image)
    plt.show()


   