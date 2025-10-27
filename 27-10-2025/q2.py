# Q2. Using OpenCV, perform the following operations on an image:
# • Display original, blurred, and edge-detected (Canny) versions side by side.
# • Print the image size, color channels, and file format.
import cv2
import numpy as np

# Load the image
image = cv2.imread("test.png")

# Display original image
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Print image properties
height, width, channels = image.shape
print(f"Image Size: {width}x{height}")
print(f"Color Channels: {channels}")
print(f"File Format: PNG")  # Assuming the file is PNG based on the filename   
# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Display blurred image
cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Display edge-detected image
cv2.imshow("Edge Detected Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Combine images side by side for comparison
combined_image = np.hstack((image, blurred_image, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)))
cv2.imshow("Original | Blurred | Edge Detected", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("result_opencv.jpg", combined_image)
print("Combined image saved as 'result_opencv.jpg'")
