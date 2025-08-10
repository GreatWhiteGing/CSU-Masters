import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Mod4CT1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

mean3 = cv2.blur(img, (3, 3))
median3 = cv2.medianBlur(img, 3)
gblur3_s0 = cv2.GaussianBlur(img, (3, 3), 0.5)
gblur3_s1 = cv2.GaussianBlur(img, (3, 3), 1.5)

mean5 = cv2.blur(img, (5, 5))
median5 = cv2.medianBlur(img, 5)
gblur5_s0 = cv2.GaussianBlur(img, (5, 5), 0.5)
gblur5_s1 = cv2.GaussianBlur(img, (5, 5), 1.5)

mean7 = cv2.blur(img, (7, 7))
median7 = cv2.medianBlur(img, 7)
gblur7_s0 = cv2.GaussianBlur(img, (7, 7), 0.5)
gblur7_s2 = cv2.GaussianBlur(img, (7, 7), 1.5)

titles = ["Mean Filtering (3x3)", "Median Filtering (3x3)", "Gaussian Blur Sigma 0.5 (3x3)", "Gaussian Blur Sigma 1.5 (3x3)",
          "Mean Filtering (5x5)", "Median Filtering (5x5))", "Gaussian Blur Sigma 0.5 (5x5))", "Gaussian Blur Sigma 1.5 (5x5))",
          "Mean Filtering (7x7)", "Median Filtering (7x7)", "Gaussian Blur Sigma 0.5 (7x7)", "Gaussian Blur Sigma 1.5 (7x7)"]
images = [mean3, median3, gblur3_s0, gblur3_s1,
          mean5, median5, gblur5_s0, gblur5_s1,
          mean7, median7, gblur7_s0, gblur7_s2]

for i in range(12):
    plt.subplot(3, 4, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()