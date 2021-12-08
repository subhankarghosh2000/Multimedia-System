import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('image1.jpg')
print(img)
lum_img=img[:, :, 0]

plt.imshow(img)

plt.imshow(lum_img, cmap="hot")
plt.savefig('output.jpg', bbox_inches='tight')
plt.show()
