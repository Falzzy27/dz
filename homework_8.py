def tuple_create(el1, el2, *args):
    '''
    Функция принимает два или более значений и возвращает список из них
    '''
    return [el1, el2, *args]


# 1 Дан список из строк. Вывести из списка только те элементы, которые содержат символ «в»
spis = ['fawefawfwaf', 'Слово', "позже", "аббревиатура", "Произошел", "вечер", "первый"]
spis_v = [el for el in spis if el.count('в')]
print(spis_v)



# 2 Дан список из строк. Вывести список, состоящий из символов в верхнем регистре
spis = ['grgrsg','gtrgksikjg','kaofkj','KWEFAKJJEIFGEAJNG','awkfkfk','awkfkfKFAWKFKAkfawkf','skegorkgo','KWEAKFWEKFAW']
spis_final = [el for el in spis if el.isupper()]
print(spis_final)



# 3 Даны два списка чисел. Получить список, состоящий из суммы квадратов соответствующих элементов исходных списков
spis1 = [12,41,41,24,12,412,4,21,4]
spis2 = [5151,1,54,1,531,5,1,531,531,5,315]
spis_comb = list(map(tuple_create, spis1, spis2))
square = list(map(lambda x: x[0]**2+x[1]**2, spis_comb))
print(square)



# 4 Даны 3 списка чисел. Вывести список, который содержит периметр треугольника, составленного из соответствующих элементов исходных списков в том случае если это возможно, если невозможно, то 0.
spis1 = [53, 51, 5, 57, 68, 8, 3, 46, 32, 521, 654, 5, 4, 43, 6, 436, 46, 4, 64, 43, 6]
spis2 = [1, 5, 31, 5, 7, 67, 6, 23, 5, 15, 32, 65, 67, 1, 5, 31, 3, 1, 1, 2, 5, 15, 2, 51, 25]
spis3 = [6, 54, 62, 66, 2, 654, 7, 61, 6, 315, 6, 4613, 5, 3, 4, 64, 64, 6, 62, 6, 426, 426, 42]
spis_comb = list(map(tuple_create, spis1, spis2, spis3))
spis_f = [sum(el) for el in spis_comb if el[0]+el[1]>el[2] and el[1]+el[2]>el[0] and el[0]+el[2]>el[1]]
print(spis_f)