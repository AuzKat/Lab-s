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
    str(input())
    if "ф" or  "Ф" in str:
            print("Ого! Это редкое слово!")
    else:
        print("Эх,это не очень редкое слово")

def proc4():
    import random
    a = random.randint(0, 100) # вводим первую переменную в диапазоне 0-99
    b = random.randint(0, 100) # вводим вторую переменную в диапазоне 0-99
    s = a + b # s-сумма двух переменных
    print(a1, '+', b1, '=')
    o = int(input()) # выводим целое число в ответ
    if o == s: # сравниваем ответ с суммой
        print('Правильно!')
    else:
        print('Ответ неверный')

def proc41():
    import random
    error_count = 0
    count = 0
    while error_count < 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        if int(input(f"{a} + {b} = ")) == a + b:
            count += 1
            print('Правильно!')
        else:
            error_count += 1
            print('Неправильно!')
    print(f"Игра окончена. Правильных ответов {count}")