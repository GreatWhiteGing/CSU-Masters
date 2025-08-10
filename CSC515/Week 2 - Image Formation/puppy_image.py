import numpy as np
import cv2
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pylab as plt

img_mpl = plt.imread("puppy.jpg")
img_cv2 = cv2.imread("puppy.jpg")

print(img_mpl.shape)
print(img_cv2.shape)

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img_mpl)
ax.axis("off")
plt.show()

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(img_mpl[:,:,0], cmap="Reds")
axs[1].imshow(img_mpl[:,:,1], cmap="Greens")
axs[2].imshow(img_mpl[:,:,2], cmap="Blues")
axs[0].axis("off")
axs[1].axis("off")
axs[2].axis("off")
axs[0].set_title("Red channel")
axs[1].set_title("Green channel")
axs[2].set_title("Blue channel")
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img_cv2)
axs[1].imshow(img_mpl)
axs[0].axis("off")
axs[1].axis("off")
axs[0].set_title("CV BGR Image")
axs[1].set_title("Matplotlib RGB Image")
plt.show()

img_cv2_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
fig, ax = plt.subplots()
ax.imshow(img_cv2_rgb)
ax.axis("off")
ax.set_title("CV RGB Image")
plt.show()