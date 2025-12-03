from PIL import Image, ImageFilter, ImageOps, ImageEnhance


img = Image.open("yellow_car.jpg")
# print('img formate:', img.format)
# print('img formate:', img.size)
# print('img formate:', img.mode)
# img.show()

# rgb = img.convert("RGB")
# print('img formate:', rgb.mode)
# rgb.show()

# rs = img.resize((200,200))
# rs.save("ni amma.png")


# R = img.rotate(-90)
# R.show()

# cropped = img.crop((50, 50, 250, 150))
# cropped.show()
# cropped.save("cropped_safe.png")


# width, height = img.size
# print(width/2, height/2)

# gs = img.convert("JPG")
# print(gs.mode)

# gs.show()

# gm = img.convert("L")

# gm.show()

# b = img.filter(ImageFilter.BLUR)
# b.show()


# flip = ImageOps.flip(img)
# flip.show()

# mirror = ImageOps.mirror(img)
# mirror.show()

# img.show()


e = ImageEnhance.Brightness(img)
bi = e.enhance(1.5)

bi.show()




