def lab61 ():
    city_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                 "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}
    print(city_dict ["Чехия"])
    for key in sorted(city_dict):
        print(key, " - ",city_dict[key])
lab61()
def lab62 ():
        erydit = {"а": 6,
                  "б": 3, "в": 1,
                  "г": 3, "д": 3,
                  "е": 8, "ё": 3,
                  "ж": 3, "з": 5,
                  "и": 1, "й": 4,
                  "к": 2, "л": 3,
                  "м": 2, "н": 1,
                  "о": 1, "п": 2,
                  "р": 1, "с": 3,
                  "т": 1, "у": 2,
                  "ф": 10, "х": 5,
                  "ц": 5, "ч": 9,
                  "ш": 8, "щ": 10,
                  "ъ": 10, "ы": 4,
                  "ь": 6, "э": 8,
                  "ю": 8, "я": 3
                  }
        a = input("Введите слово: ")
        b = 0
        for i in a:
            b += erydit[i.lower()]
        print("Сумма: ", b)

def lab63 ():