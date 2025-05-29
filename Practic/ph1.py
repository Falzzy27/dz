
import tkinter as tk
import math


def highlight_point(canvas, x, y, ox, oy, scale=50, color="#ff6347", label=""):
    """
    Отметка точки (x, y) на графике.
    """
    cx = ox + x * scale
    cy = oy - y * scale
    radius = 6
    canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius,
                       fill=color, outline='')
    if label:
        canvas.create_text(cx, cy - 15, text=label, fill=color,
                           font=("Arial", 10, "bold"))


def draw_grid_and_axes(cnv, ox, oy, step=50, axis_color="#aaaaaa"):
    """
    Рисуем координатные оси и сетку.
    """
    w = int(cnv["width"])
    h = int(cnv["height"])

    # Вертикальные линии сетки
    for x in range(0, w, step):
        cnv.create_line(x, 0, x, h, fill="#444444")
        if abs(x - ox) > 5:
            label = str((x - ox) // step)
            cnv.create_text(x, oy + 15, text=label, fill=axis_color, font=("Arial", 9, "bold"))

    # Горизонтальные линии сетки
    for y in range(0, h, step):
        cnv.create_line(0, y, w, y, fill="#444444")
        if abs(y - oy) > 5:
            label = str(-(y - oy) // step)
            cnv.create_text(ox - 15, y, text=label, fill=axis_color, font=("Arial", 9, "bold"))

    # Оси
    cnv.create_line(0, oy, w, oy, fill=axis_color, width=2)
    cnv.create_line(ox, 0, ox, h, fill=axis_color, width=2)


def find_roots(f, a, b, step=0.1, tol=1e-4):
    """
    Поиск всех корней на отрезке [a, b] методом бисекции.
    """
    roots = []
    x = a
    while x < b:
        x1 = x
        x2 = x + step
        if f(x1) * f(x2) < 0:
            root = bisection(f, x1, x2, tol)
            if root is not None:
                roots.append(root)
        x += step
    return roots


def bisection(f, a, b, tol=1e-4):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        return None
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        fm = f(m)
        if fm == 0:
            return m
        elif fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
    return (a + b) / 2


def plot_func(cnv, func, origin_x, origin_y, scale=50, color="#1e90ff"):
    """
    Построение графика функции.
    """
    prev_point = None
    width = int(cnv["width"])
    height = int(cnv["height"])

    for screen_x in range(width):
        real_x = (screen_x - origin_x) / scale
        try:
            real_y = func(real_x)
            screen_y = origin_y - real_y * scale
        except:
            prev_point = None
            continue

        if 0 <= screen_y <= height:
            if prev_point:
                cnv.create_line(prev_point[0], prev_point[1], screen_x, screen_y,
                                fill=color, width=2)
            prev_point = (screen_x, screen_y)
        else:
            prev_point = None


def make_canvas(root_win, w=800, h=600, bg="#2e2e2e"):
    c = tk.Canvas(root_win, width=w, height=h, bg=bg, highlightthickness=0)
    c.pack(padx=20, pady=20)
    return c


def main():
    window = tk.Tk()
    window.title("График функции и корни")
    window.configure(bg="#3a3a3a")

    canvas = make_canvas(window)
    center_x, center_y = 400, 300
    scale = 80

    draw_grid_and_axes(canvas, center_x, center_y, step=scale)

    f = lambda x: -x ** 2 + 2  # Пример функции

    plot_func(canvas, f, center_x, center_y, scale=scale)

    # Показываем пересечение с осью Y (x=0)
    y_intersect = f(0)
    highlight_point(canvas, 0, y_intersect, center_x, center_y, scale, label=f"{y_intersect:.2f}")
    print(f"Пересечение с OY: (0, {y_intersect:.2f})")

    # Показываем все корни функции
    roots = find_roots(f, -5, 5)
    for r in roots:
        highlight_point(canvas, r, 0, center_x, center_y, scale, label=f"{r:.2f}")
        print(f"Корень найден: x = {r:.4f}")

    window.mainloop()


if __name__ == "__main__":
    main()
