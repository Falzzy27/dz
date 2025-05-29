# -*- coding:utf-8 -*-
# Вспомогательная функция для 6 задания
def gen_employees(lines: int, filename: str = 'employees.txt', language: str = "ru_RU"):
    """
        Для работы функции необходимо установить faker --> pip install Faker
        Функция создания файла из lines строк, содержащих Имена Фамилию и дату рождения
        На вход принимает:
        lines: количество строк
        filename: название которое дастся файлу
        language: язык вида "len_LEN" ("ru_RU", "en_US", ...)
        Доступные языки можно найти здесь: https://faker.readthedocs.io/en/master/
        Возвращает: пусто
    """
    from faker import Faker

    fake = Faker(language)
    f = open(filename, 'w+')
    for i in range(lines):
        pers = fake.name().split()
        if '.' in pers[0] or '-' in pers[0]:
            pers = fake.name().split()
            f.write(pers[0] + ' ' + pers[1] + ' ' + str(fake.date_of_birth()) + '\n')
        else:
            f.write(pers[0] + ' ' + pers[1] + ' ' + str(fake.date_of_birth()) + '\n')
    f.close()


# 1 Написать функцию, которая по переданной ей дате определяет, является ли год этой даты високосным.
def leap_year(data: str = None) -> bool:
    """
        Функция определяющая является ли введенный год високосным
        На вход принимает строку содержащую дату (dd-mm-yyyy)
        Возвращает: True если год високосный, иначе False
    """
    import datetime

    if data is None:
        year = int(datetime.datetime.now().strftime('%Y'))
    else:
        if type(data) != int:
            year = int(data[-4:])
        else:
            year = data
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


# 2 Вычислить количество дней (часов/минут), прошедших с начала года.
def time_since_boty(data: str, type_out: str) -> int:
    import datetime
    """
        Функция определяющая количество дней (часов/минут) с начала года до указанной даты этого же года
        На вход принимает строки:
        data: дата (dd-mm-yyyy) или год
        type: 'days', 'hours', 'minutes'
        Возвращает: количество дней (часов/минут), прошедших с начала года
    """
    if data == int:
        year_start = datetime.datetime(int(data), 1, 1)
    else:
        year_start = datetime.datetime(int(data[-4:]), 1, 1)
    diff = datetime.datetime.now() - year_start
    print(diff)

    if type_out == "days":
        return diff.days
    elif type_out == "hours":
        return diff.days * 24 + diff.seconds // 3600
    elif type_out == "minutes":
        return diff.days * 24 * 60 + diff.seconds // 60


# 3 Вычислить количество секунд, прошедших с начала эпохи Unix (1 января 1970).
def unix_to_now():
    """
        Функция определяющая количество секунд с начала эпохи Unix до текущего времени
        На вход принимает: Пусто
        Возвращает: количество секунд с начала эпохи Unix
    """
    import datetime

    time_now = datetime.datetime.now()
    unix = datetime.datetime(1970, 1, 1)
    diff = time_now - unix
    print(diff.seconds + diff.days * 24 * 60 * 60)


# 4 Написать  функцию – русифицированный аналог strftime(), которая работает также как strftime(),
# только имена дней недели и месяцев выдаёт на русском языке.
def rus_strftime(param: str) -> str:
    """
        Русифицированная функция-аналог strftime()
        На вход принимает: param содержащий код формата для strftime()
        Возвращает то же, что и strftime() на русском
    """
    import datetime

    B = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
         'Декабрь']
    A = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    b = ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сент', 'Окт', 'Ноя', 'Дек']
    a = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

    date = (datetime.datetime.now().date())

    if '%A' in param:
        param = param.replace('%A', A[date.weekday()])
    elif '%B' in param:
        param = param.replace('%B', B[date.month - 1])
    elif '%a' in param:
        param = param.replace('%a', a[date.weekday()])
    elif '%b' in param:
        param = param.replace('%b', b[date.month - 1])
    elif '%c' in param:
        param = param.replace('%c', a[date.weekday()] + ' ' + b[date.month - 1] + ' ' + date.strftime('%d %X %Y'))
    return date.strftime(param)


# 5 Дан список студентов, содержащий их фамилии, имена и даты рождения (dd.mm.yyyy). Напишите программу,
# которая будет находить самого старшего студента из этого списка и выводить его фамилию, имя и дату рождения,
# а если имеется несколько старших студентов с одинаковой датой рождения, то определять их дату рождения и количество.
# Пример: “Иванов Иван 12.09.2000”, и т.д.
def sp_elder(file='employees.txt') -> list[str] | str | tuple[str, int]:
    import datetime
    """
        Функция определяющая старшего(их) студента(ов)
        На вход принимает файл содержащий фамилии, имена и даты рождения студентов
        Возвращает самого старшего студента и его дату рождения, если их больше 1 возвращает дату старших и их количество
    """
    f = open(file, 'r')
    stud_spisok = f.read().split('\n')
    elder = datetime.datetime.strptime(stud_spisok[0].split()[-1], '%d.%m.%Y').date()
    elder_stud = stud_spisok[0].split()[0:2]
    age_spisok = [datetime.datetime.strptime(stud_spisok[i].split()[-1], '%d.%m.%Y').date() for i in
                  range(len(stud_spisok))]
    count_eld = 1

    for el in age_spisok:
        if str(el) < str(elder):
            elder = el
            elder_stud = stud_spisok[age_spisok.index(el)]
            count_eld = 1
        elif str(el) == str(elder):
            count_eld += 1
    f.close()
    if count_eld == 1:
        return elder_stud
    return str(elder), count_eld


# 6 Дан список сотрудников организации с указанием их фамилии, имени и даты рождения.
# Администрация ежедневно поздравляет всех сотрудников, родившихся в этот день. Напишите программу,
# которая будет определять сотрудника, чей день рождения будет в ближайшие 5 дней от текущей даты.
# Программа должна выводить фамилию, имя и дату рождения сотрудника.
def bd_notif(file_or_gen: str | tuple):
    """
        Функция оповещающая о днях рождения сотрудников в ближайшие 5 дней
        На вход принимает имя файла содержащего имена, фамилии и даты рождения(yyyy-mm-dd)
        или кортеж (int, 'name') для генерации случайного списка содержащего n-ое количество сотрудников и их даты рождения
        Выводит: фамилии и даты рождения сотрудников чьи дни рождения в ближайшие 5 дней
    """
    import datetime
    if type(file_or_gen) is tuple:
        gen_employees(file_or_gen[0], file_or_gen[1])
        file_or_gen = 'employees.txt'

    f = open(file_or_gen)
    peoples = f.read().split('\n')
    f.close()

    date_now = str(datetime.datetime.now().date())[5:].split('-')
    spisok_age = [peoples[i][-10:] for i in range(len(peoples) - 1)]
    age_spisok_dt, birth = [], []

    for i in range(len(peoples) - 1):
        age_spisok_dt.append(
            str(datetime.date(int(spisok_age[i][:4]), int(spisok_age[i][5:7]), int(spisok_age[i][-2:])))[5:].split('-'))
    for i in range(len(age_spisok_dt)):
        diff = int(date_now[1]) - int(age_spisok_dt[i][1])
        if date_now[0] == age_spisok_dt[i][0] and 1 <= diff <= 5:
            if diff == 1:
                print(f'{peoples[i][:-10]}- день рождения через {diff} день')
            if diff == 5:
                print(f'{peoples[i][:-10]}- день рождения через {diff} дней')
            if 2 <= diff <= 4:
                print(f'{peoples[i][:-10]}- день рождения через {diff} дня')


# 7 Для заданного года посчитать количество выходных дней в этом году (то есть количество суббот и воскресений).
def weekend(year: int = None) -> int:
    """
        Функция считающая количество выходных дней в году
        На вход принимает year - год для которого необходимо посчитать количество выходных
        (если вход пустой берет текущую дату)
        Возвращает количество выходных
    """
    import datetime

    if year is None:
        year = datetime.datetime.now().year

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = [5, 6]
    SS = 0
    if leap_year(str(year)):
        for i in range(len(leap_year_days)):
            for d in range(1, leap_year_days[i] + 1):
                if datetime.date(year, i + 1, d).weekday() in weekdays:
                    SS += 1
    else:
        for i in range(len(days)):
            for d in range(1, days[i] + 1):
                if datetime.date(year, i + 1, d).weekday() in weekdays:
                    SS += 1
    return SS


# 8 Написать программу, которая выводит на экран календарь на месяц в виде таблицы, столбцами которой являются недели.
# На вход программе подаётся год и месяц или дата.
def calendar_table(d_or_ym: str | tuple | None = None):
    """
        Функция выводящая на экран календарь на текущий месяц в виде таблицы
        На вход идет:
        кортеж содержащий месяц и год (year, month)
        or дату вида (yyyy-mm-dd)
        or Пусто
        Выводит: календарь на текущий месяц в виде таблицы
    """
    import datetime

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    curr_day = 1
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декабрь']

    if d_or_ym is None:
        date = datetime.datetime.now().date().timetuple()
        d_or_ym = (date[0], date[1])
    if type(d_or_ym) is str:
        d_or_ym = tuple(int(i) for i in d_or_ym.split('-')[:-1])
    print('~~~~~~~~~~~~~~~~~~~~')
    print(f'    {months[int(d_or_ym[1]) - 1]} {d_or_ym[0]}')
    print('~~~~~~~~~~~~~~~~~~~~')
    print('Пн Вт Ср Чт Пт Сб Вс')
    if leap_year(d_or_ym[0]):
        date = datetime.date(d_or_ym[0], d_or_ym[1], 1).weekday()
        for _ in range(date):
            print('   ', end='')
        for _ in range(7 - date):
            print(f'{curr_day:2d}', end=' ')
            curr_day += 1
        print()
        while curr_day <= leap_year_days[d_or_ym[1]]:
            for _ in range(7):
                print(f'{curr_day:2d}', end=' ')
                curr_day += 1
            print()
    else:
        date = datetime.date(d_or_ym[0], d_or_ym[1], 1).weekday()
        for _ in range(date):
            print('   ', end='')
        for _ in range(7 - date):
            print(f'{curr_day:2d}', end=' ')
            curr_day += 1
        print()
        while curr_day <= days[d_or_ym[1]]:
            for _ in range(7):
                print(f'{curr_day:2d}', end=' ')
                curr_day += 1
            print()


if __name__ == '__main__':
    # 1
    print(leap_year('11.06.1660'))

    # 2
    print(time_since_boty('11-03-1660', 'days'))
    print(time_since_boty('11-03-1660', 'hours'))
    print(time_since_boty('11-03-1660', 'minutes'))

    # 3
    print(unix_to_now)

    # 4
    print(rus_strftime('%B'))
    print(rus_strftime('%A'))
    print(rus_strftime('%b'))
    print(rus_strftime('%a'))
    print(rus_strftime('%c'))

    # 5
    print(sp_elder('stud.txt'))

    # 6
    bd_notif((1000, 'employees.txt'))

    # 7
    print(weekend())

    # 8
    calendar_table()
    calendar_table((988, 7))
    calendar_table('988-07-28')
