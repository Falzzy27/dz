from math import sqrt



# (1) Пользователь вводит число. Проверить знак введённого числа и выдать соответствующее сообщение
try:
    number = float(input())
except ValueError: print('Введенное значение является строкой')
else:
    if number > 0: print('Введенное число положительное')
    elif number == 0: print('Введенное число равно нулю')
    else: print('Введенное число отрицательное')





# (2) Пользователь вводит 3 числа. Программа проверяет могут ли эти числа являться сторонами треугольника
try:
    num_1, num_2, num_3 = float(input()), float(input()), float(input())
except ValueError: print('Введенное значение является строкой')
else:
    if num_1+num_2 > num_3 and num_1+num_3 > num_2 and num_2+num_3 > num_1: print('Треугольник с такими значениями может существовать')
    else: print('Такой треугольник существовать не может')





# (3) Пользователь вводит число. Программа выдаёт сообщение о чётности/нечётности введённого числа.
try:
    number = float(input())
except ValueError: print('Введенное значение является строкой')
else:
    if number%2 == 0: print('Введенное число четное')
    else: print('Введенное число нечетное')





#(4) Определить, является ли введённое пользователем число квадратом какого-либо числа.
try:
    number = float(input())
except ValueError: print('Введенное значение является строкой')
else:
    if sqrt(number)**2 == number: print('Введенное число является квадратом ' + str(sqrt(number)))
    else: print('Число не является квадратом какого-либо числа')





# (5) Пользователь вводит три числа – коэффициенты квадратного уравнения. Программа вычисляет корни уравнения.
try:
    num_1, num_2, num_3 = float(input()), float(input()), float(input())
except ValueError: print('Введенное значение является строкой')
else:
    discriminant = num_2**2 - 4*num_1*num_3
    if discriminant < 0: print('Корни данного уровнения не существуют')
    else:
        x1, x2 = ((-num_2+sqrt(discriminant))/(2*num_1)), ((-num_2-sqrt(discriminant))/(2*num_1))
        print(x1, x2)





# (6) Написать программу, проверяющую является ли введённое пользователем число целым или дробным.
try:
    num = float(input())
except ValueError: print('Введенное значение является строкой')
else:
    if float(num).is_integer(): print('Введенное число целое')
    elif not float(num).is_integer(): print('Введенное число дробное')





# (7) Пользователь вводит два числа. Программа проверяет делится ли первое число на второе
try:
    num_1, num_2 = float(input()), float(input())
except ValueError: print('Введенное значение является строкой')
else:
    if num_1%num_2 == 0: print('Первое число делится на второе')
    else: print('Первое число не делится на второе, остаток: ' + str(num_1%num_2))





# (8) Пользователь вводит символ. Программа проверяет является ли этот символ цифрой, буквой или чем-то другим.
try:
    num = float(input())
except ValueError: print('Введенное значение является строковым типом данных')
else:
    if float(num).is_integer(): print('Введенное число является целым типом данных')
    elif not float(num).is_integer(): print('Введенное число является дробным типом данных')
    else: print('Введенное значения ялвяется логическим типом данных')





# (9) Пользователь вводит три числа. Программа выводит максимальное из них.
try: num_1, num_2, num_3 = float(input()), float(input()), float(input())
except ValueError: print('Введенное значение является строкой')
else: print(max(num_1, num_2, num_3))





# (10) Написать программу вычисления количества положительных чисел среди введённых пользователем трёх чисел.
try:
    nums = []
    count = 0
    for i in range(3): nums.append(float(input()))
except ValueError: print('В вводе присутсвует строковый тип данных')
else:
    for i in range(len(nums)):
        if nums[i] >= 0:
            count += 1
    print(count)





# (11) Пользователь вводит координаты точки на плоскости (x,y). Определить в какой четверти или на какой оси декартовой плоскости находится точка
try: coords = list(map(float, input().split()))
except ValueError: print('Введенное значение является строкой')
else:
    if len(coords) != 2: print('Нужно ввести 2 элемента')
    else:
        if coords[0] > 0 and coords[1] > 0: print('Точка находится в I четверти')
        elif coords[0] < 0 and coords[1] > 0: print('Точка находится в II четверти')
        elif coords[0] < 0 and coords[1] < 0: print('Точка находится в III четверти')
        elif coords[0] > 0 and coords[1] < 0: print('Точка находится в IV четверти')
        elif coords[0] == 0 and coords[1] == 0: print('Точка находится на начале координат')
        elif coords[0] == 0 and coords[1] > 0 or coords[1] < 0: print('Точка находится на оси Y')
        elif coords[0] < 0 or coords[0] > 0 and coords[1] == 0: print('Точка находится на оси X')





# (12) Определить, является ли введённое пользователем число целым квадратом какого-либо числа.
try: num = float(input())
except ValueError: print('Введенное значение является строкой')
else:
    if not float(num).is_integer(): print('Введенное число дробное')
    else:
        if sqrt(num)**2 == num: print('Число является целым квадратом числа ' + str(int(sqrt(num))))
        else: print('Число не является целым квадратом какого-либо числа')