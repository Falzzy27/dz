import random


# 1 Написать функцию, которая создает файл, содержащий n строк из m цифр и букв. (цифры или буквы зависит от параметра)


def file_create(lines, amount, type_w):
    """
        Функция создания файла из lines строк и amount количества цифр/букв
        type принимает параметр 'nums', 'str' или 'all' которыми определяется из чего будет состоять файл
        'nums' - только цифры
        'str' - только символы латинского алфавита обоих регистров
        'all' - цифры и символы латинского алфавита
        Возвращает: пусто
    """
    digit = [i for i in range(10)]
    alph = [chr(i) for i in range(65, 123) if i < 91 or i > 96]
    temporary_line = ''

    file1 = open('file.txt', 'w')
    for i in range(lines):

        # Если требуется список из чисел
        if type_w == 'nums':
            line = [str(random.randint(0, 9)) for empty in range(amount)]
            for el in line:
                temporary_line += el
            file1.write(temporary_line + '\n')

        # Если требуется список из символов
        elif type_w == 'str':
            line = [random.choice(alph) for empty in range(amount)]
            for el in line:
                temporary_line += el
            file1.write(temporary_line + '\n')

        # Если требуется список из чисел/символов
        elif type_w == 'all':
            line = [random.choice(alph + digit) for empty in range(amount)]
            for el in line:
                temporary_line += str(el)
            file1.write(temporary_line + '\n')

        temporary_line = ''
    file1.close()


file_create(100, 300, 'nums')  # nums / str / all


# 2 Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем записать их произведение в файл output.txt.
def file_multi(file='input.txt'):
    """
        Функция создающая файл содержащий произведение первых 10 чисел записанных через пробел
        На ввод идет относительный или абсолютный путь к файлу
        Возвращает: пусто
    """
    file = open(file, 'r')
    a = 1
    temp = ''
    count = 0
    flag = False

    spisok = [i for i in file.read()]
    if spisok[-1].isdigit():
        spisok += ' '
    for i in spisok:
        if count == 10:
            break
        if i.isdigit():
            temp += i
        elif i == ' ':
            a *= int(temp)
            temp = ''
            count += 1

    file_final = open('output.txt', 'w')
    file_final.write(str(a))
    file_final.close()
    file.close()


# 3 В файле записаны целые числа. Найти максимальное и минимальное число и записать в другой файл.
def max_min(file='start_file.txt'):
    """
        Функция создающая файл содержащий минимальное и максимальное число файла поданного на ввод
        На ввод идет относительный или абсолютный путь к файлу
        Возвращает: пусто
    """
    file = open(file, 'r')
    temp = ''
    start_spisok = [el for el in file.read()]
    spisok = []

    if start_spisok[-1].isdigit():
        start_spisok += ' '

    for el in start_spisok:
        if el.isdigit():
            temp += el
        if el == ' ':
            if temp.isdigit():
                spisok.append(temp)
                temp = ''
    n = open('file_max_min.txt', 'w')
    n.write(
        'Максимальное число:' + str(max(map(int, spisok))) + '\n' + 'Минимальное число:' + str(min(map(int, spisok))))
    n.close()
    file.close()


# 4 В текстовом файле записаны сведения о детях детского сада в следующем формате:
#       Иванов Иван 5 лет
#       Необходимо записать в другой текстовый файл самого старшего и самого младшего.
def age_filter(file='children_info.txt'):
    """
        Функция создающая файл содержащий старшего(их) и младшего(их) детей из
        поданного на ввод файла состоящего из сведений о детях
        На ввод идет относительный или абсолютный путь к файлу
        Возвращает: пусто
    """
    file = open(file, 'r', encoding="utf-8")
    temp_age = ''
    ages = []
    file_spisok = [i for i in file]
    for el in file_spisok:
        for i in el:
            if i.isdigit():
                temp_age += i
            else:
                if temp_age.isdigit():
                    ages.append(temp_age)
                    temp_age = ''

    file_final = open('finish_file.txt', 'w')
    file_final.write('Старший(е):\n')
    for i in range(len(file_spisok)):
        if file_spisok[i].count(' ' + str(max(map(int, ages))) + ' '):
            file_final.write(file_spisok[i])

    file_final.write('\nМладший(е):\n')

    for i in range(len(file_spisok)):
        if file_spisok[i].count(' ' + str(min(map(int, ages))) + ' '):
            file_final.write(file_spisok[i])
    file_final.close()
    file.close()


# 5 Дан файл, состоящий из цифр и других символов.  Подсчитать сумму чисел этого файла
def summ_file(file='file.txt'):
    """
        Функция суммирования чисел из файла
        На ввод идет относительный или абсолютный путь к файлу
        Возвращает: сумму чисел из файла
    """
    file = open(file, 'r')
    summ = 0
    temp_el = ''
    for el in file:
        for i in el:
            if i.isdigit():
                temp_el += i
            else:
                if temp_el.isdigit():
                    summ += int(temp_el)
                    temp_el = ''
    print(summ)
