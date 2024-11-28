# 1 Написать функцию, для поиска минимума двух чисел.
def minimal(num1, num2):
    """
    Функция поиска минимума двух чисел
    Принимает на ввод 2 числа, возвращает минимальное из этой пары чисел
    """
    if num1 > num2:
        return num2
    else:
        return num1


print(minimal(float(input()), float(input())))



# 2 Написать функцию, для поиска максимума трёх чисел.
def max_of_3(num1, num2, num3):
    """
    Функция поиска максимума двух чисел
    Принимает на ввод 2 числа, возвращает максимальное из этой пары чисел
    """
    if num1 <= num2 >= num3:
        return num2
    elif num1 <= num3 >= num2:
        return num3
    else:
        return num1


print(max_of_3(10,4,2))



# 3 Написать функцию для суммирования чисел списка.
def summator(spis):
    summ = 0
    """
    Функция суммирования чисел списка
    Принимает на ввод список и суммирует элементы из этого списка
    """
    for element in spis:
        summ += element
    return summ

print(summator([1,24,1,5,15,51,5,15]))



# 4 Написать функцию для перемножения чисел списка.
def multiple(spis):
    summ = 1
    """
    Функция перемножения чисел списка
    Принимает на ввод список и перемножает все его элементы
    """
    for element in spis:
        summ *= element
    return summ


print(multiple([1, 5, 15, 1, 5, 5, 4, 25,]))



# 5 Написать функцию для обращения строки.
def revers_stroki(stoka):
    final = ''
    """
    Функция обращения строки
    Принимает на ввод строку и возвращает её в перевернутом виде
    """
    for i in range(len(stoka)-1, -1, -1):
        final += stoka[i]
    return final


print(revers_stroki('Перевернутая строка'))



# 6 Написать функцию для вычисления факториала числа. Функция принимает число в качестве аргумента.
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


print(factorial(11))


# 7 Написать функцию проверки, находится ли число в заданном диапазоне.
def inclusion(num, start, end):
    """
    Функция проверки включения числа в диапазон
    Принимает на ввод число и диапазон значений, выводит результат проверки на вхождение числа в данный диапазон
    """
    if start < num < end:
        return True
    else:
        return False


print(inclusion(110, 3, 23))
print(inclusion(10, 3, 23))



# 8 Написать функцию, которая суммирует все целые числа в указанном диапазоне от start до end. Если start больше чем end, то поменять их местами.
def summator_Z(start, end):
    summ = 0
    if start > end:
        start, end = end, start
    for i in range(start, end+1):
        summ += i
    return summ


print(summator_Z(1, 11))
print(summator_Z(11, 1))