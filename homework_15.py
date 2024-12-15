import tkinter as tk


def SOC(x, y, lmx, lmy, lpx, lpy, ex, ey, ox_color=None, oy_color=None):
    """
        Функция создания ДПСК
        На вход принимает:
        x, y - размеры холста (в мм)
        lmx, lmy, lpx, lpy - длины осей абсциссы и ординаты в соответствущих направлениях (в см)
        ex, ey - единичные отрезки на осях X и Y соответственно
        ox_color, oy_color (необязательные аргументы) - цвета осей X и Y соответственно
    """
    # Начало координат
    xc = x / 2
    yc = y / 2

    # масштабирующий множитель
    nm = 10

    # цена деления в пикселях/мм
    xnm = ex * nm
    ynm = ey * nm

    # Настройки и создание холста
    root = tk.Tk()
    root.title("Coordinate system")
    root.geometry(f"{x}x{y}")
    canvas = tk.Canvas(bg='white', width=x, height=y)
    canvas.pack()

    # Создание линий осей
    # x в отрицательных значениях
    canvas.create_line(xc - lmx - 5, yc, xc, yc, fill=ox_color)
    # y в отрицательных значениях
    canvas.create_line(xc, yc + lmy + 5, xc, yc, fill=oy_color)
    # x в положительных значениях
    canvas.create_line(xc, yc, xc + lpx, yc, fill=ox_color)
    # y в положительных значениях
    canvas.create_line(xc, yc, xc, yc - lpy, fill=oy_color)

    # Создание стрелок
    canvas.create_line(xc + lpx - 10, yc - 7, xc + lpx, yc, fill=ox_color)
    canvas.create_line(xc + lpx - 10, yc + 7, xc + lpx, yc, fill=ox_color)
    canvas.create_line(xc, yc - lpy, xc - 7, yc - lpy + 10, fill=oy_color)
    canvas.create_line(xc, yc - lpy, xc + 7, yc - lpy + 10, fill=oy_color)

    # Создание делений
    # деления на отрицательном направлении оси x
    xnowm = xc + nm
    for i in range(lmx // xnm):
        canvas.create_line(xnowm - xnm, yc - 4, xnowm - xnm, yc + 5, fill=ox_color)
        xnowm -= xnm
    # деления на отрицательном направлении оси y
    ynowm = yc
    for i in range(lmy // ynm):
        canvas.create_line(xc - 4, ynowm + ynm, xc + 5, ynowm + ynm, fill=oy_color)
        ynowm += ynm
    # деления на положительном направлении оси x
    xnowp = xc - nm
    for i in range((lpx // xnm) - 1):
        canvas.create_line(xnowp + xnm, yc - 4, xnowp + xnm, yc + 5, fill=ox_color)
        xnowp += xnm
    # деления на положительном направлении оси y
    ynowp = yc
    for i in range((lpy // ynm) - 1):
        canvas.create_line(xc - 4, ynowp - ynm, xc + 5, ynowp - ynm, fill=oy_color)
        ynowp -= ynm

    # Начало координат
    canvas.create_text(xc - nm, yc + nm, text='0')
    # Символы X и Y
    canvas.create_text(xc + lpx, yc + nm, text='X')
    canvas.create_text(xc + nm, yc - lpy, text='Y')

    # цена деления
    # на +x
    xnowp = xc - nm
    enx = ex
    for i in range((lpx // xnm) - 1):
        canvas.create_text(xnowp + xnm, yc + 10, text=f'{enx}')
        xnowp += xnm
        enx += ex
    # на +y
    ynowp = yc
    eny = ey
    for i in range((lpy // ynm) - 1):
        canvas.create_text(xc + 15, ynowp - ynm, text=f'{eny}')
        ynowp -= ynm
        eny += ey
    # на -x
    xnowm = xc + nm
    enx = -1 * ex
    for i in range(lmx // xnm):
        canvas.create_text(xnowm - xnm, yc + 10, text=f'{enx}')
        xnowm -= xnm
        enx -= ex
    # на -y
    ynowm = yc
    enx = -1 * ey
    for i in range(lmy // ynm):
        canvas.create_text(xc + 15, ynowm + ynm, text=f'{enx}')
        ynowm += ynm
        enx -= ey

    tk.mainloop()


if __name__ == '__main__':
    SOC(1000, 800, 200, 200, 300, 300, 6, 8, 'red', 'purple')
