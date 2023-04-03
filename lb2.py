def lb11():
    print('Введите пароль:')

    a=input()
    b=input()

    if a==b:
        print('Пароль совпадает')
    else:
        print('Пароль не совпадает')


def lb12():
    password = input('Введите пароль:')
    if len(password) < 6:
        print('Слишком короткий пароль')
    elif password[0:7] == "abricos":
        print('Ненадёжный пароль')
    else:
        print('Надёжный пароль')

def lb13():
    password = input('Введите пароль')
    is_numeric = False
    is_upper = False
    is_lower = False
    is_spec = False

    for char in password:
        if char.isnumeric():
            is_numeric = True
        elif char.islower():
            is_lower = True
        elif char.isupper():
            is_upper = True
        elif char in "@#%&":
            is_spec = True
    if len(password) > 4 and is_numeric and is_upper and is_lower and is_spec:
        print('Пароль: подходит')
    else:
        print('Пароль прост')

def lb21():
    n = int(input('Ввод номера места:'))
    print()
    if n > 36:
        print('Ваше место - боковое')
    elif n % 2:
        print('Ваше место в купе внизу')
    else:
        print('Ваше место в купе наверху')

def lb22():
    n = int(input('Ввод номера места:'))
    print()
    if n > 36:
        print('Ваше место - боковое')
    elif n % 2:
        print('Ваше место в купе внизу')
    else:
        print('Ваше место в купе наверху')

def lb23():
    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('Високосный')
    else:
        print('Не високосный')

def lb24():
    colors = ('красный', 'синий', 'желтый')
    c1 = input()
    c2 = input()
    if c1 in colors and c2 in colors:
        if c1 != c2:
            if (c1 in ("красный", "синий")) and (c2 in ("красный", "синий")):
                print("фиолетовый")
        elif (c1 in ("желтый", "красный")) and (c2 in ("желтый", "красный")):
            print("оранжевый")
        elif (c1 in ("синий", "желтый")) and (c2 in ("синий", "желтый")):
            print("зеленый")
        else:
            print(c1)
    else:
        print("ошибка цвета")
        