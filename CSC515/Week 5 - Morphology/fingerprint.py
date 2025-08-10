import cv2
import numpy as np
from matplotlib import pyplot as plt

kernel = np.ones((5, 5), "uint8")

img = cv2.imread("fingerprint.jpg")
blur = cv2.GaussianBlur(img, (5, 5), 0)
dilation = cv2.dilate(img, kernel=kernel, iterations=1)
erosion = cv2.erode(img, kernel=kernel, iterations=1)
open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel=kernel)
close_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel=kernel)
close_blur = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel=kernel)
close_dilation = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel=kernel)
close_erosion = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel=kernel)
titles = ["Original", "Gaussian Blur", "Dilation", "Erosion", "Opening", "Closing", "Closing on Gaussian", "Closing on Dilation", "Closing on Erosion"]

images = [img, blur, dilation, erosion, open_img, close_img, close_blur, close_dilation, close_erosion]

for i in range(9):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()