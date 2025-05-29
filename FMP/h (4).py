# 1 Организовать ввод элементов списка с клавиатуры. Размер списка также должен задаваться пользователем. Введённый список вывести на экран.
spisok = [input() for i in range(int(input('Введите количество элементов списка:')))]
print(spisok)



# 2 Дан список, состоящий из n элементов. Вывести элементы списка на экран (в столбик, в строку)
spisok = [input() for i in range(int(input('Введите количество элементов списка:')))]
print(*spisok)
print()
for element in spisok:
    print(element)



# 3 Дан список из n чисел. Вывести элементы списка, которые больше 7.
spisok = [input() for i in range(int(input('Введите количество элементов списка:')))]
for element in spisok:
    if int(element) > 7:
        print(element, end=' ')



# 4 Дан список из n элементов. Вывести элементы, у которых чётный (нечётный) индекс
spisok = [input() for i in range(int(input('Введите количество элементов списка:')))]
for index in range(0, len(spisok), 2):
    print(spisok[index], end=' ')
print()
for index in range(1, len(spisok), 2):
    print(spisok[index], end=' ')



# 5 Дан список из n элементов. Вывести элементы списка по три в строке.
spisok = [input() for i in range(int(input('Введите количество элементов списка:')))]
for i in range(0, len(spisok), 3):
    print(spisok[i:i+3])



# 6 Дан список чисел. Найти среднее арифметическое элементов списка.
spisok = [int(input()) for i in range(int(input('Введите количество элементов списка:')))]
print(sum(spisok)/len(spisok))



# 7 Дан список из n чисел. Вывести сумму всех чётных элементов списка
spisok = [int(input()) for i in range(int(input('Введите количество элементов списка:')))]
summ = 0
for element in spisok:
    if element % 2 == 0:
        summ += element
print(summ)



# 8 Дан список из n чисел. Вывести сумму элементов списка, которые делятся на 4
spisok = [int(input()) for i in range(int(input('Введите количество элементов списка:')))]
summ = 0
for element in spisok:
    if element % 4 == 0:
        summ += element
print(summ)



# 9 Дан список из n чисел. Вывести произведение всех ненулевых элементов списка
spisok = [int(input()) for i in range(int(input('Введите количество элементов списка:')))]
multi = 1
for element in spisok:
    if element != 0:
        multi *= element
print(multi)



# 10 Дан список чисел. Вывести элементы списка, последняя цифра которых равна 2.
spisok = [int(input()) for i in range(int(input('Введите количество элементов списка:')))]
for element in spisok:
    if element % 10 == 2:
        print(element, end=' ')



# 11 Дан список из n чисел. Вывести номера всех максимальных элементов списка.
spisok = [int(input()) for i in range(int(input('Введите количество элементов списка:')))]
for index in range(len(spisok)):
    if max(spisok) == spisok[index]:
        print(index, end=' ')