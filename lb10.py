import json

def z_1(): # Открытие файла и загрузка данных из JSON
    with open("/Users/katrine/Desktop/ works/уник/10/products.json") as F:
        data = json.load(F) # Извлечение списка продуктов
    products = data['products'] # Перебор продуктов и вывод информации на экран
    for product in products:
        print("Название: {}".format(product['name']))
        print("Цена: {}".format(product['price']))
        print("Вес: {}".format(product['weight']))
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")

def z_2(): #есть возможность добавить своё
        with open("/Users/katrine/Desktop/ works/уник/10/products.json") as f:
            file2 = json.load(f)
        name = input("Введите название продукта: ")
        price = int(input("Введите цену продукта: "))
        weight = int(input("Введите вес продукта: "))
        available = input("Есть ли продукт в наличии?") == 'да'
        newspisok = {"name": name, "price": price, "available": available, "weight": weight}
        file2["products"].append(newspisok)  # добавление словаря в начальный список
        with open('/Users/katrine/Desktop/ works/уник/10/products.json', 'w', encoding='utf-8') as f:
            json.dump(file2, f)  # добавление нового списка в начальный файл
        print("Обновленный список:")
        with open('/Users/katrine/Desktop/ works/уник/10/products.json') as f:
            data = json.load(f)
            for product in data['products']:
                print(f"Название: {product['name']}")
                print(f"Цена: {product['price']}")
                print(f"Вес: {product['weight']}")
                if product['available']:
                    print("В наличии")
                else:
                    print("Нет в наличии")
                print()
def z_3():
    # Открытие файла en-ru.txt и чтение данных
    with open('en-ru.txt', 'r', encoding='utf-8') as F:
        data = F.readlines() # Создание пустого словаря
    ru_en_dict = {}   # Разделение строк на пары "русское слово - английское слово"
    for line in data:
        words = line.strip().split(" - ")
        en_words = words[0].split(",")
        ru_word = words[1]
        for en_word in en_words:
            ru_en_dict[ru_word] = ru_en_dict.get(ru_word, []) + [en_word] # Сортировка ключей словаря по алфавиту
    sorted_ru_words = sorted(ru_en_dict.keys()) # Создание и запись данных в файл ru-en.txt
    with open('ru-en.txt', 'w', encoding='utf-8') as F:
        for ru_word in sorted_ru_words:
            en_words = ", ".join(sorted(ru_en_dict[ru_word]))
            F.write("{} - {}\n".format(ru_word, en_words))
print(z_3())
