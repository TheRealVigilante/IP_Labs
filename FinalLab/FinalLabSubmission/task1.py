import sys
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

# Check if the image path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python task1.py <image_path>")
    sys.exit(1)

# Get the image path from the command-line argument
path = sys.argv[1]
image = io.imread(path)

# User Input
r_change = int(input("Enter the value of r_change: "))
g_change = int(input("Enter the value of g_change: "))
b_change = int(input("Enter the value of b_change: "))

inversion = input("Do you want to invert the image? (yes/no): ")

brightness_scaling = float(input("Enter the value of brightness scaling factor: "))

def change_colour(image, r_change, g_change, b_change):
    image = image.astype(np.int16)  # Convert to int16 to prevent overflow
    image[:, :, 0] = np.clip(image[:, :, 0] + r_change, 0, 255)
    image[:, :, 1] = np.clip(image[:, :, 1] + g_change, 0, 255)
    image[:, :, 2] = np.clip(image[:, :, 2] + b_change, 0, 255)
    return image.astype(np.uint8)  # Convert back to uint8

def invert(image, inversion):
    if inversion.lower() == "yes" or inversion.lower() == "y":
        image = 255 - image
    return image

def brightness(image, brightness_scaling):
    image = image.astype(np.float32)  # Convert to float32 for scaling
    image = np.clip(image * brightness_scaling, 0, 255)
    return image.astype(np.uint8)  # Convert back to uint8

colour_changed = change_colour(image, r_change, g_change, b_change)
inverted = invert(colour_changed, inversion)
bright_adjusted = brightness(inverted, brightness_scaling)

# Plot the different images (can be ignored, just written to make sure the results are satisfactory)
# fig, ax = plt.subplots(1, 4, figsize=(15, 5))
# ax[0].imshow(image)
# ax[0].set_title("Original Image")
# ax[1].imshow(colour_changed)
# ax[1].set_title("Colour Changed")
# ax[2].imshow(inverted)
# ax[2].set_title("Inverted")
# ax[3].imshow(bright_adjusted)
# ax[3].set_title("Brightness Adjusted")
# plt.show()

def save_image(image, path):
    io.imsave(path, image)

save_image(bright_adjusted, "task1_output.png")

def report():
    print(f"R: {r_change}")
    print(f"G: {g_change}")
    print(f"B: {b_change}")
    print(f"Inversion: {inversion}")
    print(f"Brightness Scaling Factor: {brightness_scaling}")
    print()
    print("Steps Performed:")
    print("Step 1: Colour Change (all channels together)")
    print("Step 2: Inverted the image (if selected)")
    print("Step 3: Adjusted the brightness using the scaling factor given")
    print("Step 4: Image saved at task1_output.png")

report()