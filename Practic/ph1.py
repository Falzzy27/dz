import tkinter as tk
import math


def highlight_root(canvas, x_root, ox, oy, scale=50, color="#ff6347"):
    """
    Отмечаем на графике найденный корень уравнения.
    """
    cx = ox + x_root * scale
    cy = oy
    radius = 6
    canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, fill=color, outline='')
    canvas.create_text(cx, cy - 15, text=f"{x_root:.3f}", fill=color, font=("Arial", 10, "bold"))


def draw_grid_and_axes(cnv, ox, oy, step=50, axis_color="#aaaaaa"):
    """
    Рисуем координатные оси и легкую сетку на холсте.
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

    # Рисуем оси
    cnv.create_line(0, oy, w, oy, fill=axis_color, width=2)
    cnv.create_line(ox, 0, ox, h, fill=axis_color, width=2)


def find_root_bisection(f, left, right, tol=1e-4):
    """
    Методом бисекции ищем корень уравнения f(x) = 0 на отрезке [left, right].
    Возвращаем None, если корень отсутствует.
    """
    val_left = f(left)
    val_right = f(right)

    if val_left * val_right > 0:
        return None

    while (right - left) / 2 > tol:
        mid = (left + right) / 2
        val_mid = f(mid)
        if val_mid == 0:
            return mid
        elif val_left * val_mid < 0:
            right = mid
            val_right = val_mid
        else:
            left = mid
            val_left = val_mid
    return (left + right) / 2


def plot_func(cnv, func, origin_x, origin_y, scale=50, color="#1e90ff"):
    """
    Рисуем график функции func на canvas cnv.
    """
    prev_point = None
    width = int(cnv["width"])
    height = int(cnv["height"])

    for screen_x in range(width):
        real_x = (screen_x - origin_x) / scale
        try:
            real_y = func(real_x)
            screen_y = origin_y - real_y * scale
        except Exception:
            prev_point = None
            continue

        if 0 <= screen_y <= height:
            if prev_point is not None:
                cnv.create_line(prev_point[0], prev_point[1], screen_x, screen_y, fill=color, width=2, smooth=True)
            prev_point = (screen_x, screen_y)
        else:
            prev_point = None


def make_canvas(root_win, w=800, h=600, bg="#2e2e2e"):
    """
    Создаем и возвращаем холст с заданными параметрами.
    """
    c = tk.Canvas(root_win, width=w, height=h, bg=bg, highlightthickness=0)
    c.pack(padx=20, pady=20)
    return c


def main():
    window = tk.Tk()
    window.title("Функциональный график")
    window.configure(bg="#3a3a3a")

    canvas = make_canvas(window)
    center_x, center_y = 400, 300
    scale = 50

    draw_grid_and_axes(canvas, center_x, center_y, step=scale)

    f = lambda x: -x ** 2 + 2
    plot_func(canvas, f, center_x, center_y, scale=scale)

    root_val = find_root_bisection(f, -2, 2)
    if root_val is not None:
        highlight_root(canvas, root_val, center_x, center_y, scale=scale)
        print(f"Корень найден: x = {root_val:.4f}")

    y_intersect = f(0)
    print(f"Пересечение с Y: (0, {y_intersect})")

    window.mainloop()


if __name__ == "__main__":
    main()
