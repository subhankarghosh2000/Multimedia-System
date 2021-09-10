import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('image1.jpg')

print(img)

lum_img=img[:, :, 1]

plt.imshow(lum_img, cmap="nipy_spectral")

plt.savefig('output.jpg', bbox_inches='tight')

plt.show()