def lb51(num):
    num = int(num)
    x = [2, 3, 4, 5, 6]
    if num in x:
        print('Поздравляю, Вы угадали число!')
    else:
        print('Нет такого числа!')


def lb52():
    ls = [2, 3, 4, 4, 5]
    duplicate = {str(x) for x in ls if ls.count(x) > 1}
    x = lambda: print('nothing')
    y = lambda: print(' '.join(duplicate))
    x() if len(duplicate) < 1 else y()


def lb53():
    week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sun', 'Sut')
    weekends = int(input())
    print('Weekends:', week[:-weekends - 1:-1])
    print('Work days:', week[:-weekends])
    print()



