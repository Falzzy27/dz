"""# (1) Вывод всех четных чисел от 2 до 100 включительно
for nums in range(2,  101, 2):
    print(nums)



# (2) Программа, вычисляющая сумму квадратов всех чисел от 1 до N
try: nums = int(input('Введите число: '))
except ValueError: print('Введите число, на ввод была подана строка или вещественное число')
else:
    summ = 0
    for num in range(1, nums+1):
        summ += num**2
    print(summ)



# (3) Сумма всех нечетных чисел от 1 до 99
summ = 0
for num in range(1, 99, 2):
    summ += num
print(summ)



# (4) Подсчет количества цифр вводимого целого неотрицательного числа
try: num = int(input('Введите число: '))
except ValueError: print('Введите число, на ввод была подана строка или вещественное число')
else:
    if num > 0:
        print(len(str(num)))
    else:
        print('На ввод было подано отрицательное число')



# (5) Cумма квадратов первых N четных натуральных чисел
try:
    num = int(input('Введите число:'))
except ValueError: print('Введите число, на ввод была подана строка или вещественное число')
else:
    print(num*(num+1))



# (6) Вычислить 1+2+4+8+…+256
num, summ = 1, 0
while num <= 256:
    summ += num
    num *= 2
print(summ)

# OR
print(256*2-1)



# (7) Вычислить (1+2)*(1+2+3)*…*(1+2+…+10)
multiplication, num = 1, 1
for i in range(2, 11):
    multiplication *= num + i
    num += i
print(multiplication)
"""


# (8) Вводятся данные о росте N учащихся. Определить средний рост учащихся
heigh = []
try:
    childs = int(input('Введите кол-во учащихся: '))
except ValueError: print('Введите целое число, на ввод была подана строка или вещественное число')
else:
    index = [i for i in range(1, childs+1)]
    for i in range(childs):
        try: heigh.append(float(input('Введите рост ученика ' + str(index[i]) + ': ')))
        except ValueError: break
    try:
        print(sum(heigh) / len(heigh))
    except ZeroDivisionError: pass
