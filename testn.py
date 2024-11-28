# -*- coding:utf-8 -*-
from datetime import timedelta, datetime

# 1.  Написать функцию, которая по переданной ей дате определяет, является ли год этой даты високосным.
date = input("Введите месяц, день и год через тире: ")


def check(date):
    "Функция в качестве агумента принимает строку date, содержащую в себе дату и определяет, является ли введенный год високосным.\nВ случае, если год високоный, возвращает строку, сообщающую об этом(так же в случае с не високосным годом)"
    y = datetime.strptime(date, '%m-%d-%Y')
    d = timedelta(days=365)
    next = y - d
    day_p = int(y.strftime("%d"))
    day_f = int(next.strftime("%d"))
    if day_p != day_f:
        return "Введелнный вами год является високосным"
    else:
        return "Введелнный вами год не является високосным"


# 2.  Вычислить количество дней (часов/минут), прошедших с начала года.
def calculation():
    date = datetime.today()
    date_past = datetime(2024, 1, 1)
    # print (date_past, date)
    delta = date - date_past
    return "Количество дней, прошедших с начала года", delta.days, "Количество часов, прошедших с начала года", delta.total_seconds() // 3600, "Количество минут, прошедших с начала года", delta.total_seconds() // 60


# 3.  Вычислить количество секунд, прошедших с начала эпохи Unix (1 января 1970).
def counter():
    present = datetime.now()
    past = datetime(1970, 1, 1)
    delta = present - past
    return "Количество секунд, прошедших с начала года", delta.total_seconds()


if __name__ == '__main__':
    print(check(date))
    print(calculation())
    print(counter())
