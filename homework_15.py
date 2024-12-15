import tkinter as tk


def SOC(x, y, lmx, lmy, lpx, lpy, ex, ey, ox_color=None, oy_color=None):
    """
        ������� �������� ����
        �� ���� ���������:
        x, y - ������� ������ (� ��)
        lmx, lmy, lpx, lpy - ����� ���� �������� � �������� � �������������� ������������ (� ��)
        ex, ey - ��������� ������� �� ���� X � Y ��������������
        ox_color, oy_color (�������������� ���������) - ����� ���� X � Y ��������������
    """
    # ������ ���������
    xc = x / 2
    yc = y / 2

    # �������������� ���������
    nm = 10

    # ���� ������� � ��������/��
    xnm = ex * nm
    ynm = ey * nm

    # ��������� � �������� ������
    root = tk.Tk()
    root.title("Coordinate system")
    root.geometry(f"{x}x{y}")
    canvas = tk.Canvas(bg='white', width=x, height=y)
    canvas.pack()

    # �������� ����� ����
    # x � ������������� ���������
    canvas.create_line(xc - lmx - 5, yc, xc, yc, fill=ox_color)
    # y � ������������� ���������
    canvas.create_line(xc, yc + lmy + 5, xc, yc, fill=oy_color)
    # x � ������������� ���������
    canvas.create_line(xc, yc, xc + lpx, yc, fill=ox_color)
    # y � ������������� ���������
    canvas.create_line(xc, yc, xc, yc - lpy, fill=oy_color)

    # �������� �������
    canvas.create_line(xc + lpx - 10, yc - 7, xc + lpx, yc, fill=ox_color)
    canvas.create_line(xc + lpx - 10, yc + 7, xc + lpx, yc, fill=ox_color)
    canvas.create_line(xc, yc - lpy, xc - 7, yc - lpy + 10, fill=oy_color)
    canvas.create_line(xc, yc - lpy, xc + 7, yc - lpy + 10, fill=oy_color)

    # �������� �������
    # ������� �� ������������� ����������� ��� x
    xnowm = xc + nm
    for i in range(lmx // xnm):
        canvas.create_line(xnowm - xnm, yc - 4, xnowm - xnm, yc + 5, fill=ox_color)
        xnowm -= xnm
    # ������� �� ������������� ����������� ��� y
    ynowm = yc
    for i in range(lmy // ynm):
        canvas.create_line(xc - 4, ynowm + ynm, xc + 5, ynowm + ynm, fill=oy_color)
        ynowm += ynm
    # ������� �� ������������� ����������� ��� x
    xnowp = xc - nm
    for i in range((lpx // xnm) - 1):
        canvas.create_line(xnowp + xnm, yc - 4, xnowp + xnm, yc + 5, fill=ox_color)
        xnowp += xnm
    # ������� �� ������������� ����������� ��� y
    ynowp = yc
    for i in range((lpy // ynm) - 1):
        canvas.create_line(xc - 4, ynowp - ynm, xc + 5, ynowp - ynm, fill=oy_color)
        ynowp -= ynm

    # ������ ���������
    canvas.create_text(xc - nm, yc + nm, text='0')
    # ������� X � Y
    canvas.create_text(xc + lpx, yc + nm, text='X')
    canvas.create_text(xc + nm, yc - lpy, text='Y')

    # ���� �������
    # �� +x
    xnowp = xc - nm
    enx = ex
    for i in range((lpx // xnm) - 1):
        canvas.create_text(xnowp + xnm, yc + 10, text=f'{enx}')
        xnowp += xnm
        enx += ex
    # �� +y
    ynowp = yc
    eny = ey
    for i in range((lpy // ynm) - 1):
        canvas.create_text(xc + 15, ynowp - ynm, text=f'{eny}')
        ynowp -= ynm
        eny += ey
    # �� -x
    xnowm = xc + nm
    enx = -1 * ex
    for i in range(lmx // xnm):
        canvas.create_text(xnowm - xnm, yc + 10, text=f'{enx}')
        xnowm -= xnm
        enx -= ex
    # �� -y
    ynowm = yc
    enx = -1 * ey
    for i in range(lmy // ynm):
        canvas.create_text(xc + 15, ynowm + ynm, text=f'{enx}')
        ynowm += ynm
        enx -= ey

    tk.mainloop()


if __name__ == '__main__':
    SOC(1000, 800, 200, 200, 300, 300, 6, 8, 'red', 'purple')
