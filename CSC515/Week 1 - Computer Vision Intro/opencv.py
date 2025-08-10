import cv2
import os
import platform

input_image_name = "brain.jpg"

if platform.system() == "Linux": # We are in WSL
    # This path maps to your Windows C: drive
    output_directory = f"/mnt/c/Users/bherg/Desktop"
else:
    # If for some reason you run this directly on Windows
    output_directory = os.path.join(os.path.expanduser("~"), "Desktop")

# --- Ensure the output directory exists ---
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created output directory: {output_directory}")

# --- Main Script ---
def process_image(image_name):
    # 1. Construct the full path to the input image
    # Assuming the image is in the same directory as the script for simplicity
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    input_image_path = os.path.join(current_script_dir, image_name)

    print(f"Attempting to read image from: {input_image_path}")

    # 2. Import (Read) the image
    # cv2.imread returns a NumPy array representing the image
    # The second argument can be:
    #   cv2.IMREAD_COLOR (1): Loads a color image. Any transparency of image will be neglected. This is the default.
    #   cv2.IMREAD_GRAYSCALE (0): Loads image in grayscale mode.
    #   cv2.IMREAD_UNCHANGED (-1): Loads image as is, including alpha channel.
    img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)

    # Check if the image was loaded successfully
    if img is None:
        print(f"Error: Could not read the image. Check the path and file name: {input_image_path}")
        print("Make sure 'example_image.jpg' (or your image) is in the same folder as this script, or provide its full path.")
        return

    print(f"Image '{image_name}' loaded successfully. Dimensions: {img.shape}")

    # 3. Display the image
    # 'Original Image' is the name of the window that will pop up
    cv2.imshow('Original Image', img)

    # Wait for a key press (0 means wait indefinitely)
    # This keeps the image window open until you press any key
    print("Displaying image. Press any key to close the window and continue...")
    cv2.waitKey(0)
    cv2.destroyAllWindows() # Close all OpenCV windows

    # 4. Define the output file path for the copy
    output_image_name = f"copy_of_{image_name}"
    output_image_path = os.path.join(output_directory, output_image_name)

    print(f"Attempting to write image copy to: {output_image_path}")

    # 5. Write a copy of the image
    # cv2.imwrite returns True on success, False on failure
    success = cv2.imwrite(output_image_path, img)

    if success:
        print(f"Image copy successfully written to: {output_image_path}")
    else:
        print(f"Error: Could not write the image copy to: {output_image_path}")
        print("Check if the output directory exists and if you have write permissions.")

# --- Run the script ---
if __name__ == "__main__":
    process_image(input_image_name)
