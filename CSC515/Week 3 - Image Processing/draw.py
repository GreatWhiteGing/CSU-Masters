import cv2

# --- Configuration ---
image_path = 'brett.JPG' 

# Paths to the Haar Cascade XML files
face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
eye_cascade_path = cv2.data.haarcascades + 'haarcascade_eye.xml'

# Colors (BGR format)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)

# --- Load Classifiers ---
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

img = cv2.imread(image_path)

# --- Preprocessing ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# --- Face Detection ---
# detectMultiScale(image, scaleFactor, minNeighbors)
# scaleFactor: Parameter specifying how much the image size is reduced at each image scale.
# minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it.
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7, minSize=(120, 120))

# --- Process Detected Faces ---
for (x, y, w, h) in faces:
    # Draw green circle around the face
    center_x = x + w // 2
    center_y = y + h // 2
    radius = int(max(w, h) * 0.6)
    cv2.circle(img, (center_x, center_y), radius, GREEN, 2)

    # Define the Region of Interest (ROI) for the face
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    # Detect eyes within the face ROI
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.35, minNeighbors=6, minSize=(25, 25))

    for (ex, ey, ew, eh) in eyes:
        # Draw red bounding box over the eyes (relative to the original image)
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), RED, 2)

# --- Display Result ---
cv2.imshow('this is me', img)
cv2.waitKey(0) # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()