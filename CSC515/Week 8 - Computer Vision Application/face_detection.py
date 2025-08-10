import cv2
import numpy as np
from matplotlib import pyplot as plt

panda_img_original = cv2.imread("red_panda.jpg")
far_img_original = cv2.imread("people_far.jpg")
close_img_original = cv2.imread("person_close.jpg")

panda_img_processed = panda_img_original.copy()
far_img_processed = far_img_original.copy()
close_img_processed = close_img_original.copy()

panda_img_gray = cv2.cvtColor(panda_img_original, cv2.COLOR_BGR2GRAY)
far_img_gray = cv2.cvtColor(far_img_original, cv2.COLOR_BGR2GRAY)
close_img_gray = cv2.cvtColor(close_img_original, cv2.COLOR_BGR2GRAY)

pretrained_face_path = cv2.data.haarcascades + "/haarcascade_frontalface_alt.xml"
pretrained_eye_path = cv2.data.haarcascades + "/haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(pretrained_face_path)
eye_cascade = cv2.CascadeClassifier(pretrained_eye_path)

face1 = face_cascade.detectMultiScale(panda_img_gray, scaleFactor=1.05, minNeighbors=5, minSize=(40,40))
face2 = face_cascade.detectMultiScale(far_img_gray, scaleFactor=1.05, minNeighbors=5, minSize=(40,40))
face3 = face_cascade.detectMultiScale(close_img_gray, scaleFactor=1.05, minNeighbors=5, minSize=(40,40))

for (x, y, w, h) in face1:
    cv2.rectangle(panda_img_processed, (x,y), (x+w, y+h), (0,0,255), 2)


far_img_for_display = far_img_processed.copy()

if len(face2) > 0:
    min_x = min(f[0] for f in face2)
    min_y = min(f[1] for f in face2)
    max_x = max(f[0] + f[2] for f in face2)
    max_y = max(f[1] + f[3] for f in face2)

    padding_x = int((max_x - min_x) * 0.1)
    padding_y = int((max_y - min_y) * 0.1)

    x1_zoom = max(0, min_x - padding_x)
    y1_zoom = max(0, min_y - padding_y)
    x2_zoom = min(far_img_original.shape[1], max_x + padding_x)
    y2_zoom = min(far_img_original.shape[0], max_y + padding_y)

    far_img_zoomed = far_img_original[y1_zoom:y2_zoom, x1_zoom:x2_zoom].copy()
    far_img_zoomed_gray = far_img_gray[y1_zoom:y2_zoom, x1_zoom:x2_zoom]

    target_width = 600
    if far_img_zoomed.shape[1] > 0:
        scale_ratio = target_width / far_img_zoomed.shape[1]
        new_height = int(far_img_zoomed.shape[0] * scale_ratio)
        far_img_zoomed = cv2.resize(far_img_zoomed, (target_width, new_height), interpolation=cv2.INTER_LINEAR)
        far_img_zoomed_gray = cv2.resize(far_img_zoomed_gray, (target_width, new_height), interpolation=cv2.INTER_LINEAR)

    faces_in_zoomed = face_cascade.detectMultiScale(far_img_zoomed_gray, scaleFactor=1.05, minNeighbors=5, minSize=(40,40))
    
    for (x_z, y_z, w_z, h_z) in faces_in_zoomed:
        cv2.rectangle(far_img_zoomed, (x_z,y_z), (x_z+w_z, y_z+h_z), (0,0,255), 2)

        eye_search_offset_y = int(h_z * 0.20)
        eye_search_height = int(h_z * 0.40)
        eye_search_height = max(1, min(eye_search_height, h_z - eye_search_offset_y))

        roi_gray_zoomed_eyes = far_img_zoomed_gray[y_z + eye_search_offset_y : y_z + eye_search_offset_y + eye_search_height, x_z : x_z + w_z]
        roi_color_zoomed_eyes = far_img_zoomed[y_z + eye_search_offset_y : y_z + eye_search_offset_y + eye_search_height, x_z : x_z + w_z]

        eyes_zoomed = eye_cascade.detectMultiScale(roi_gray_zoomed_eyes, scaleFactor=1.05, minNeighbors=3, minSize=(30,30))

        for (ex_z, ey_z, ew_z, eh_z) in eyes_zoomed:
            eye_roi_zoomed = roi_color_zoomed_eyes[ey_z:ey_z+eh_z, ex_z:ex_z+ew_z]
            blurred_eye_zoomed = cv2.GaussianBlur(eye_roi_zoomed, (45, 45), 0)
            roi_color_zoomed_eyes[ey_z:ey_z+eh_z, ex_z:ex_z+ew_z] = blurred_eye_zoomed
            
    far_img_for_display = far_img_zoomed
else:
    print("No faces detected in far_img. Displaying original far_img without zoom or eye blur.")


for (x, y, w, h) in face3:
    cv2.rectangle(close_img_processed, (x,y), (x+w, y+h), (0,0,255), 2)

    eye_search_offset_y = int(h * 0.20)
    eye_search_height = int(h * 0.40)
    eye_search_height = max(1, min(eye_search_height, h - eye_search_offset_y))

    roi_gray_close_eyes = close_img_gray[y + eye_search_offset_y : y + eye_search_offset_y + eye_search_height, x : x + w]
    roi_color_close_eyes = close_img_processed[y + eye_search_offset_y : y + eye_search_offset_y + eye_search_height, x : x + w]

    eyes_close = eye_cascade.detectMultiScale(roi_gray_close_eyes, scaleFactor=1.05, minNeighbors=3, minSize=(30,30))

    for (ex, ey, ew, eh) in eyes_close:
        eye_roi_close = roi_color_close_eyes[ey:ey+eh, ex:ex+ew]
        blurred_eye_close = cv2.GaussianBlur(eye_roi_close, (95, 95), 0)
        roi_color_close_eyes[ey:ey+eh, ex:ex+ew] = blurred_eye_close

original_images_rgb = [
    cv2.cvtColor(panda_img_original, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(far_img_original, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(close_img_original, cv2.COLOR_BGR2RGB)
]
original_titles = ["Original Panda", "Original Far", "Original Close"]

processed_images_rgb = [
    cv2.cvtColor(panda_img_processed, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(far_img_for_display, cv2.COLOR_BGR2RGB),
    cv2.cvtColor(close_img_processed, cv2.COLOR_BGR2RGB)
]
processed_titles = ["Panda (Face Detection)", "Far Image (Zoomed & Eyes Blurred)", "Close Image (Eyes Blurred)"]

all_images_for_display = original_images_rgb + processed_images_rgb
all_titles_for_display = original_titles + processed_titles

plt.figure(figsize=(15, 10))

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(all_images_for_display[i])
    plt.title(all_titles_for_display[i])
    plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()