# -*- coding: utf-8 -*-
# 2 Написать функцию, которая выводит список файлов заданного каталога,
# с указанием размеров файлов и даты их последней модификации
def dir_fsm(path: str) -> list:
    """
      Функция создающая список файлов из поданного на вход каталога

      На вход принимает абсолютный путь до файла path

      Возвращает: Список состоящий файлы, их размер и дату последнего изменения
    """
    import os.path, datetime, time

    dir_list = os.listdir(path)
    os.chdir(path)
    spisok = []

    for i in dir_list:
        dt = str(datetime.datetime.strptime(time.ctime(os.path.getmtime(i)), '%a %b %d %H:%M:%S %Y'))
        if os.path.isdir(i):
            spisok.append('folder' + ' | ' + dt + ' | ' + i)
        else:
            spisok.append(str(os.path.getsize(i)) + ' bytes' + ' | ' + dt + ' | ' + i)
    return spisok


# 3 Написать функцию, которая создает резервную копию заданного файла/каталога
# в имени резервной копии должны использоваться дата и время создания резервной копии
def backup(path: str, dir_to: str = None):
    """
        Функция создающая резервную копию файла/каталога

        На вход принимает:

        path - абсолютный путь до файла, для которого требуется создать резервную копию

        to(необязательный параметр): путь, куда необходимо загрузить резервную копию

        если 'to' пусто: резервная копия сохранится в папке, откуда произошел вызов

        Возвращает: пусто
    """
    import os, datetime, shutil, zipfile
    backup_time = datetime.datetime.now().strftime('%Y-%m-%d   %H_%M_%S')

    zip_file = zipfile.ZipFile(f'{path.split('\\')[-1]} (backup {backup_time}).zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zip_file.write(os.path.join(root, file))
    zip_file.close()

    if dir_to is not None:
        shutil.move(os.path.abspath(f'{path.split('\\')[-1]} (backup {backup_time}).zip'), dir_to)


# 4 Написать Функцию, которая рисует дерево каталогов заданного каталога
def cat_tree(path: str):
    """
        Функция рисующая дерево каталогов заданного каталога

        На вход принимает абсолютный путь до каталога (path)

        Выводит: дерево каталогов заданного каталога
    """
    import os.path

    def h_f(temp):
        for el in temp:
            if el.split(' | ')[0] == 'folder':
                return True
            return False

    def recurs_print(path_dir, k=0):
        direct = dir_fsm(path_dir)
        tab = '    ' * k
        dir_sort = sorted(direct, reverse=True)
        if h_f(dir_sort):
            for i in dir_sort:
                if i.split(' | ')[0] == 'folder':
                    print(tab + os.path.abspath(i.split(' | ')[2]))
                    recurs_print(os.path.abspath(i.split(' | ')[2]), k + 1)
                    os.chdir('..')
        else:
            if not dir_sort:
                pass
            else:
                for i in dir_sort:
                    print(f'{tab} {i}', sep='\n')

    recurs_print(path)


# 5 Написать аналог команды cat (OS Linux)
def cat(*args: str):
    """
        Функция являющаяся аналогом команды cat (OS Linux)

        На вход принимает параметры схожие с параметрами cat

        Выход\возврат зависит от параметров
    """
    import os, time
    spisok = []
    for i in args:
        if os.path.isfile(i):
            f = open(f'{i}', 'r')
            temp = [i for i in f.read().split('\n')]
            f.close()
            spisok = spisok + temp

    def n(el):
        sp = []
        for index, item in enumerate(el):
            sp.append(str(index + 1) + ' ' + item)
        return sp

    def sort(el):
        el.sort()
        return el

    def more(el):
        for index in el:
            print(index)
            time.sleep(0)

    def less(el):
        for index in el:
            print(index)
            time.sleep(0.3)

    def new_f(el, index):
        file = open(f'{index[1:]}', 'w')
        for index in el:
            file.write(index + '\n')
        file.close()

    if '--number' in args or '-n' in args:
        spisok = n(spisok)
    if '|sort' in args:
        spisok = sort(spisok)
    if '|more' in args:
        more(spisok)
    if '|less' in args:
        less(spisok)
    for i in args:
        if '>' in i:
            new_f(spisok, i)
    return spisok


if __name__ == '__main__':
    # 2
    # print(*dir_fsm(r'C:\Program Files (x86)'), sep='\n')
    # 3
    # backup(r'C:\Windows\ru-RU')
    # backup(r'C:\Program Files (x86)')
    # 4
    # cat_tree(r'C:\Users\slano\PycharmProjects\homeworks')
    # 5
    print(*cat('-n', 'stud.txt', 'peoples.txt', '|sort', '>abs.txt'), sep='\n')
