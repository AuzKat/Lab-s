import os
from PIL import Image
import csv


def z_1():
    # Путь к папке с исходными изображениями
    input_folder = "/Users/katrine/Desktop/ works/уник/программирование/9"

    # Путь к папке для итоговых изображений
    output_folder = "/Users/katrine/Desktop/ works/уник/программирование/9"

    # Создаем папку для итоговых изображений, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Проходим по всем файлам в папке
    for filename in os.listdir(input_folder):
        # Проверяем, что файл - изображение
        if filename.endswith(".jpg"):
            # Считываем изображение
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Применяем к нему операцию (например, изменяем размер)
                new_img = img.resize((300, 300))
                # Сохраняем итоговое изображение в папку output_folder
                s="new"+filename
                new_img.save(os.path.join(output_folder, s))


def z_2():
    # Путь к папке с исходными изображениями
    input_folder = "/Users/katrine/Desktop/ works/уник/программирование/9"

    # Путь к папке для итоговых изображений
    output_folder = "/Users/katrine/Desktop/ works/уник/программирование/9"

    # Создаем папку для итоговых изображений, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Проходим по всем файлам в папке
    for filename in os.listdir(input_folder):
        # Проверяем, что файл - изображение
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Считываем изображение
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Применяем к нему операцию (например, изменяем размер)
                new_img = img.resize((500, 500))
                # Сохраняем итоговое изображение в папку output_folder
                s="new"+filename
                new_img.save(os.path.join(output_folder, s))

def z_3():
    filename = "/Users/katrine/Desktop/ works/уник/программирование/9/data.csv"

    # Создаем словарь для хранения данных
    data = {}

    # Считываем данные из CSV-файла и сохраняем их в словаре
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)  # пропускаем заголовок
        for row in reader:
            product = row[0]
            quantity = int(row[1])
            price = int(row[2])
            data[product] = {"quantity": quantity, "price": price}

    # Вычисляем итоговую сумму расходов
    total_cost = sum(data[product]["quantity"] * data[product]["price"] for product in data)

    # Выводим данные в требуемом формате
    print("Нужно купить:")
    for product in data:
        quantity = data[product]["quantity"]
        price = data[product]["price"]
        print(f"{product} - {quantity} шт. за {price} руб.")
    print(f"Итоговая сумма: {total_cost} руб.")



print(z_1())
print(z_2())
print(z_3())
