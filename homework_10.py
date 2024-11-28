# 1	Заданы два вектора. Найти расстояние между концами этих векторов
def vector_dist(vect1: tuple, vect2: tuple) -> float or bool:
    """
        Функция вычисляющая расстояние между концами двух векторов
        На вход принимает кортеж из координат концов двух векторов: vect1, vect2
        Возвращает расстояние между координатами концов векторов
    """
    if type(vect1) == tuple and type(vect1) == tuple and len(vect1) == 2 and len(vect2) == 2:
        return ((vect2[0] - vect1[0]) ** 2 + (vect2[1] - vect1[1]) ** 2) ** 0.5
    elif type(vect1) == int and type(vect2) == int or type(vect1) == float and type(vect2) == float:
        return vect1, vect2
    else:
        return False


# print(vector_dist((4, 6), (10, 2)))


# 2 Заданы два вектора. Найти диагональ параллелограмма (вектор), построенного на заданных векторах. Длину вектора и координаты конца.
def diag_parall(vect1: tuple, vect2: tuple) -> float or bool:
    """
        Функция вычисляющая длину и координаты конца диагонали параллелограмма построенного на двух векторах
        На вход принимает кортеж из координат концов двух векторов: vect1, vect2
        Возвращает длину и координаты конца диагонали параллелограмма
    """
    if vect1[0] / vect2[0] == vect1[1] / vect2[1]:
        return False
    if len(vect1) == 2 and len(vect2) == 2:
        if vect1[0] == vect2[0] and vect1[1] == vect2[1]:
            return False
        return [((vect1[0] + vect2[0]) ** 2 + (vect1[1] + vect2[1]) ** 2) ** 0.5, (
            vect1[0] + vect2[0], vect1[1] + vect2[1])]
    else:
        return False


print(diag_parall((113, 678), (511, 213)))
print(diag_parall((113, 678), (113, 678)))
print(diag_parall((113, 678, 313), (113, 678)))
print(diag_parall((2, 3), (4, 6)))
