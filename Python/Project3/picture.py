import cv2
import os

# Get the full path to the image file
image_path = os.path.join(os.getcwd(), "TAPP_Logo.png")

# Load the image
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# Check if the image was successfully loaded
if image is None:
    print("Error: Failed to load the image")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to create a mask of the foreground object
ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Apply the mask to create a transparent background
image[mask == 0] = [0, 0, 0, 0]

# Save the result
cv2.imwrite("TAPP_Logo_transparent.png", image)
