from PIL import Image
znak = "watermark.png"
with Image.open(znak) as img_znak:
    img_znak.load()

img_znak = Image.open(znak)
img_znak = img_znak.resize((img_znak.width // 2, img_znak.height // 2))

filename = "shrek.jpg"
with Image.open(filename) as img:
    img.load()

img.paste(img_znak, (200, 15), img_znak)
img.save("znak_shrek.jpg")
