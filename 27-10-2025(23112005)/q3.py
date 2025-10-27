# Q3. Combine OpenCV and Pillow in a single program to:
# • Read an image using OpenCV and display it.
# • Convert the same image to grayscale using Pillow.
# • Compare both image formats (OpenCV and PIL).
import cv2
from PIL import Image

# Read image using OpenCV
opencv_image = cv2.imread("test.png")
cv2.imshow("OpenCV Image", opencv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert to grayscale using Pillow
pil_image = Image.fromarray(cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB))
pil_image = pil_image.convert("L")
pil_image.show()
# Compare both image formats
print(f"OpenCV Image Shape: {opencv_image.shape}")  # (height, width, channels)
print(f"PIL Image Size: {pil_image.size}")  # (width, height)  
print(f"OpenCV Image Data Type: {opencv_image.dtype}")
print(f"PIL Image Mode: {pil_image.mode}")  # 'L' for grayscale
# Save the grayscale image from Pillow
pil_image.save("result_combined.jpg")
print("Combined image saved as 'result_combined.jpg'")