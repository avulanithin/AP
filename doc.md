# Image Processing with OpenCV

This project demonstrates basic image processing operations using Python and OpenCV, including resizing, grayscale conversion, blurring, and file size comparison between JPEG and PNG formats.

---

## 📌 Input Images

- `test.png`  
- `yellow_car.jpg`

---

## 🖥️ Code

```python
import cv2
import numpy as np
import os

# Read images
img = cv2.imread("test.png")
image = cv2.imread("yellow_car.jpg")

# Resize example (fixed size)
new_size = (200, 200)
resized_image = cv2.resize(img, new_size)

# Convert to grayscale
im2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Convert grayscale back to 3 channels so we can stack with color images
im2_bgr = cv2.cvtColor(im2, cv2.COLOR_GRAY2BGR)

# --- Side by side: Original and Grayscale ---
side_by_side1 = np.hstack((image, im2_bgr))
cv2.imwrite("side_by_side1.png", side_by_side1)

# --- Side by side: Original and Blurred ---
side_by_side2 = np.hstack((image, blurred_image))
cv2.imwrite("side_by_side2.png", side_by_side2)

# --- Resize the image to half of the original size ---
height, width = image.shape[:2]
new_size = (width // 2, height // 2)
resized_half = cv2.resize(image, new_size)

# Save resized image
cv2.imwrite("resized_half.png", resized_half)
cv2.imwrite("resized_half.jpg", resized_half, [cv2.IMWRITE_JPEG_QUALITY, 90])

# --- Compare file sizes ---
jpeg_size = os.path.getsize("resized_half.jpg")
png_size = os.path.getsize("resized_half.png")

print(f"JPEG file size: {jpeg_size / 1024:.2f} KB")
print(f"PNG file size:  {png_size / 1024:.2f} KB")

if jpeg_size < png_size:
    print("JPEG is smaller because it uses lossy compression.")
else:
    print("PNG is smaller because it uses lossless compression (rare for photos, common for graphics).")
