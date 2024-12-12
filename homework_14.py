# 1 Дано натуральное число. Вычислите сумму его цифр


def summator(num):
    """
        Функция вычисляющая сумму цифр числа

        На вход подается натуральное число num

        Возвращает: сумму его цифр
    """
    summ = 0

    if num == 0:
        return summ
    summ += num % 10

    return summator(num // 10) + summ


# 2 Дано натуральное число. Записать число в обратном порядке
def reverse(num):
    """
        Функция переворачивающая число

        На вход подается натуральное число num

        Возвращает: число в обратном порядке
    """
    lnum = ''
    if num == 0:
        return lnum
    lnum += str(num % 10)
    return lnum + str(reverse(num // 10))


# 3 Проверить число на простоту

def simple(num, div=None):
    """
        Функция проверяющая число на простоту

        На вход подается натуральное число num

        Возвращает: True или False
    """
    from sys import setrecursionlimit
    setrecursionlimit(1_000_000)
    div = num // 2 + 1 if div is None else div
    while div >= 2:
        if num % div == 0:

            return False
        else:
            return simple(num, div - 1)
    else:
        return True


# 4 Написать функцию, которая будет принимать натуральное число n и возвращать n-ую строку треугольника Паскаля.

# 5 Написать функцию генерации перестановок из заданного массива заданной длины


if __name__ == '__main__':
    # 1
    # print(summator(12))
    # 2
    # print(reverse(21211))
    # 3
    print(simple(133333))
