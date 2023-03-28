from PIL import Image
filename = "shrek.jpg"
with Image.open(filename) as img:
    img.load()

new_img = img.resize((img.width // 2, img.height // 2))

new_img.save("small_shrek.jpg")

converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.save("perev_shrek.jpg")
converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
converted_img.save("r_shrek.jpg")
