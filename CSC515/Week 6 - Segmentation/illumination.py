import cv2
import numpy as np
from matplotlib import pyplot as plt

light_bw = cv2.imread("light_side.jpg", 0)
dark_bw = cv2.imread("dark_side.jpg", 0)

height_l, width_l = light_bw.shape[0:2]
height_d, width_d = dark_bw.shape[0:2]

binary_l = np.zeros([height_l, width_l, 1], "uint8")

thresh = 50
        
ret, thresh_l = cv2.threshold(light_bw, thresh, 255, cv2.THRESH_BINARY)
ret, thresh_d = cv2.threshold(dark_bw, thresh, 255, cv2.THRESH_BINARY)
            
titles = ["Original Light", "Threshold 50 Light", "Original Dark", "Threshold 50 Dark"]
images = [light_bw, thresh_l, dark_bw, thresh_d]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()