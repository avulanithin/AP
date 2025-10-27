# Q1. Write a Python program using Pillow (PIL) to:
# • Load an image.
# • Convert it to grayscale.
# • Rotate it by 45° and resize it to 300×300.
# • Save the final output as ‘result_pillow.jpg’.
from PIL import Image

# Load the image
image = Image.open("test.png")

# Convert to grayscale
grayscale_image = image.convert("L")

# Rotate and resize
final_image = grayscale_image.rotate(45).resize((300, 300))
final_image.save("result_pillow.jpg")
print("Image processed and saved as 'result_pillow.jpg'")