def factorial(num):
    fact_intermediate = 1
    """
    Функция вычисления факториала числа
    Принимает на ввод число и возвращает факториал этого числа
    """
    if num < 0:
        return False
    elif num == 1 or num == 0:
        return 1
    else:
        for i in range(1, num+1):
            fact_intermediate *= i
    return fact_intermediate


# 1 Написать функцию, которая принимает два аргумента. Если аргументы – числа, то возвращает их сумму, а если строки или списки, то возвращает конкатенацию.
'???'

# 2
def parallax(cycle, direction, spisok):
    """
    Функция осуществляющая циклический сдвиг на cycle повторений и в направлении direction
    На ввод идут 3 аргумента:
    cycle - количество повторений сдвига
    direction - направление принимающее True(1) = вперед, или False(0) = назад
    spisok - список к которому применяется циклический сдвиг
    Выводится список с запрошенным сдвигом
    """
    lens = len(spisok)
    if direction == 1:
        for i in range(lens, lens-cycle, -1):
            spisok.append(spisok.pop(0))
        return spisok
    elif direction == 0:
        for i in range(0, cycle, 1):
            spisok.append(spisok.pop(0))
        return spisok


print(parallax(3, False, [21, 34, 5, 245, 244, 23, 667, 1]))
print()


# 3
def placements(n, k):
    """
    Функция вычисляющая число размещений
    На ввод идут 2 числа:
    n - количество элементов множества
    k - количество элементов размещения
    Программа выводит число размещений из n по k
    """
    if n-k >= 0:
        return factorial(n)/(factorial(n-k))
    else:
        return 'n не может быть меньше k'


print(placements(7,3))
print(placements(5,11))
print(placements(6,6))
print()


#4
def combinations(n, k):
    """
    Функция вычисляющая число сочетаний
    На ввод идут 2 числа:
    n - количество элементов множества
    k - количество элементов сочетания
    Программа выводит число сочетаний из n по k
    """
    if n-k >= 0:
        return factorial(n)/(factorial(k)*factorial(n-k))
    else:
        return 'n не может быть меньше k'


print(combinations(7,3))
print(combinations(5,11))
print(combinations(6,6))
print()



#5.	Написать программу, выводящую в консоль треугольник Паскаля.
def Pascal_triangle(lines):
    """
    Программа выводящая треугольник Паскаля
    На ввод идет количество выводимых строк
    На вывод треугольник Паскаля из lines строк
    """
    line = [1]
    space = ' '
    print((lines+1)*space, '1')
    for i in range(lines):
        line = list((nums[0]+nums[1]) for nums in zip([0]+line, line+[0]))
        print((lines-i)*space, *line, sep=' ')
    return "Finish"

print(Pascal_triangle(7))