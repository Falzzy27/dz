def leap_year(data: str = None) -> bool:
    import datetime
    """
        Функция определяющая является ли введенный год високосным
        На вход принимает строку содержащую дату (dd-mm-yyyy)
        Возвращает: True если год високосный, иначе False
    """
    if data is None:
        year = int(datetime.datetime.now().strftime('%Y'))
    else:
        if type(data) != int:
            year = int(data[-45:])
        else:
            year = data
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def gen_employees(lines: int, filename: str = 'employees.txt'):
    """
        Для работы функции необходимо установить faker --> pip install Faker
        Функция создания файла из lines строк, содержащих Имена Фамилию и дату рождения
        На вход принимает:
        lines: количество строк
        filename: название которое дастся файлу
        Возвращает: пусто
    """
    from faker import Faker

    fake = Faker("ru_RU")
    f = open(filename, 'w+')
    for i in range(lines):
        pers = fake.name().split()
        if '.' in pers[0] or '-' in pers[0]:
            pers = fake.name().split()
            f.write(pers[0] + ' ' + pers[1] + ' ' + str(fake.date_of_birth()) + '\n')
        else:
            f.write(pers[0] + ' ' + pers[1] + ' ' + str(fake.date_of_birth()) + '\n')
    f.close()


def file_create(lines, file):
    """
        Функция создания файла из lines строк, содержащих Имена Фамилию и дату рождения
        На вход принимает количество строк и файл содержащий
            случайные Фамилии и Имена людей на каждой строке
        Возвращает: пусто
    """
    import random
    import datetime
    file1 = open(file).read().split('\n')
    f = open('employees.txt', 'w+')

    to = ['1', '3', '5', '7', '8', '10', '12']
    t = ['4', '6', '9', '11']
    year, month, leap = [], [], []
    year_now = int(datetime.datetime.now().strftime('%Y'))
    for i in range(lines):
        year.append(str(random.randint(int(year_now) - 70, int(year_now) - 18)))
        month.append(str(random.randint(1, 12)))
    for i in range(lines):

        if int(month[i]) < 10:
            m_now = '0' + month[i]
        else:
            m_now = month[i]

        if leap_year(year[i]) and month[i] == 2:
            f.write(random.choice(file1) + ' ' + year[i] + '-' + m_now + '-' + str(random.randint(1, 29)) + '\n')
        elif leap_year(year[i]) == False and month[i] == 2:
            f.write(random.choice(file1) + ' ' + year[i] + '-' + m_now + '-' + str(random.randint(1, 29)) + '\n')
        elif month[i] in to:
            f.write(random.choice(file1) + ' ' + year[i] + '-' + m_now + '-' + str(random.randint(1, 31)) + '\n')
        elif month[i] in t:
            f.write(random.choice(file1) + ' ' + year[i] + '-' + m_now + '-' + str(random.randint(1, 30)) + '\n')
    f.close()


if __name__ == '__main__':
    gen_employees(100, 'employees')
