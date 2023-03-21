def div3(number: int): #
    return True if number % 3 == 0 else False

def div_100_by(number):
    res = None
    try:
        res = 100 / float(number)
    except ValueError:
        print("Введите число:")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except Exception as e:
        print("Неверно", e)
    return res

def magic_date_check(date: str):
    try:
        date = date.split(".")
        if int(date[0]) * int(date[1]) == int(date[2][2:]):
            return True
        else:
            return False
    except:
        print("Введите дату в формате дд.мм.гггг")

def ticket(ticket: str):
    sum1 = sum([int(i) for i in ticket[:int(len(ticket) / 2)]])
    sum2 = sum([int(i) for i in ticket[:int(len(ticket) / 2):]])
    if sum1 == sum2:
        return True
    else:
        return False