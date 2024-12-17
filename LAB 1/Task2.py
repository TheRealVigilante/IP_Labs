InputPath = input("Enter the Path of the original image")
Modification = int(input("Enter the desired change level: (0-255)"))
OutputPath = input("Enter the Path of the modified image")

#InputPath = "puppy.jpg"
Img = iio.imread(InputPath)
#print(Img.shape)

for i in range(Img.shape[0]):
    for j in range(Img.shape[1]):
        #Img[i,j,2] = 255
        Img[i,j,2] = Modification

plt.imshow(Img)
iio.imwrite(OutputPath, Img)