def proc1():
    n = int(input("ввод кол слов:"))  # вводим количество слов
    result = " "  # переменная с результатом
    for i in range(n):  # цикл в количестве n от первой строки
        w = input(f"ввод слов {i + 1}:")  # переменная которая принимает, значение
        result += w + " "  # прибавляем ко второй строке значение строки w
    print("результат:", result.strip())  # выводим результат

def proc2():
    n = int(input("ввод кол слов:"))
    result = []
    for i in range(n):
        result.append(str(input()))

    result = []
    while(new_word := str(input())) != "stop":
        result.append(new_word)
        print(" ".join(result))


def proc3():
    result = []
    while (new_word := str(input())) != "stop":
        if "ф" in new_word or  "Ф" in new_word:
            print("Ого! Это редкое слово!")
    else:
        print("Эх,это не очень редкое слово")
