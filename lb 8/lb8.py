def lb81():
    from PIL import Image
    img = Image.open("HNY.jpg")

    img_cropped = img.crop((150, 30, 840, 370))
    img_cropped.save("crop_HNY.jpg")

def lb82():
    from PIL import Image
    d = {1: "HB.jpg", 2: "march.jpg", 3: "HNY.jpg", 4: "23.jpg"}
    print(" 1 - ДР"
    " 2 - 8 марта"
    " 3 - Новый год"
    " 4 - 23 февраля")
    ans = int(input("Введите число - номер праздника : "))
    filename = d[ans]
    with Image.open(filename) as img:
        img.load()
        img.show()

def lb83():
    from PIL import Image, ImageDraw, ImageFont
    name = input("Введите имя именинника:")
    filename = "HB.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("arial_bold.ttf", 20)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 2 - 100,15),
        name + " , с праздником!",
        font=font,
        fill=("#000000")
    )
    img.show()
    img.save(name + "nameHB.jpg")

