# (1) Программа вычисления степени числа A с натуральным показателем N, без операции возведения в степень
num, degree = int(input('Введите число: ')), int(input('В какую степень возвести число?: '))
answer = 1
for i in range(1, degree+1):
    answer *= num
print(num, 'в степени', degree, '=', answer)



# (2) Программа вычисляющую A*B, не используя операцией умножения
num1, num2 = (int(input('Введите число 1: ')), int(input('Введите число 2: ')))
multiple = 0
for i in range(1, num2 + 1):
    multiple += num1
print('Произведение', num1, 'на', num2, '=', multiple)




# (3) Для заданного числа N составьте программу вычисления суммы S=1+1/2+1/3+1/4+…+1/N, где N – натуральное число.
number, summ = int(input('Введите число: ')), 0
for num in range(1, number+1):
    summ += num**(-1)
print('Сумма:', summ)



# (4) Программа, рассчитывающая количество бактерий на заданное целое значение времени.
time, bact_count = int(input('Введите время: ')), 1
for i in range(1, time + 1):
    bact_count *= 2
print('Бактерий за', time, 'минут(ы):', bact_count)



# (5) Вывести кубы целых чисел от A до B.
num1, num2 = int(input('Введите число 1: ')), int(input('Введите число 1: '))
for num in range(num1+1, num2):
    cube = num**3
    print(cube)



# (6) Сумма n-го количества элементов ряда 1, -0.5, 0.25, -0.125, …
number, summ = int(input('Введите число: ')), 1
for num in range(1, number + 1):
    summ += (-1/2)**num
print('Сумма =', summ)