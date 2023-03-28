from PIL import Image, ImageFilter
filenames = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

for file in filenames:
    with Image.open(file) as img:
        img.load()
        new_img = img.filter(ImageFilter.EDGE_ENHANCE)
        new_img.save("new_"+ file)