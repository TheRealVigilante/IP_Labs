five = iio.imread(uri="eight.tif")
five[1,2]=1.0
five[3,0]=1.0
print(five)
plt.imshow(five)