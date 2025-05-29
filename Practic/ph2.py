import tkinter as tk
import math


def make_canvas(root, width=900, height=650, bg_color="#1e1f2b"):
    """Создаем холст с необычным фоном."""
    canvas = tk.Canvas(root, width=width, height=height, bg=bg_color, highlightthickness=0)
    canvas.pack(padx=25, pady=25)
    return canvas


def draw_axes_and_grid(cnv, ox, oy, step=60, axis_color="#f0f0f0"):
    """Рисуем светлые оси и более мягкую сетку."""
    w, h = int(cnv["width"]), int(cnv["height"])

    # Вертикальная сетка (тонкая)
    for x in range(0, w, step):
        cnv.create_line(x, 0, x, h, fill="#555566", dash=(2, 4))
        if abs(x - ox) > 3:
            cnv.create_text(x, oy + 20, text=str((x - ox) // step), fill=axis_color, font=("Helvetica", 10, "italic"))

    # Горизонтальная сетка (тонкая)
    for y in range(0, h, step):
        cnv.create_line(0, y, w, y, fill="#555566", dash=(2, 4))
        if abs(y - oy) > 3:
            cnv.create_text(ox - 20, y, text=str(-(y - oy) // step), fill=axis_color, font=("Helvetica", 10, "italic"))

    # Оси (более яркие и толстые)
    cnv.create_line(0, oy, w, oy, fill=axis_color, width=3)
    cnv.create_line(ox, 0, ox, h, fill=axis_color, width=3)


def plot_function(cnv, func, origin_x, origin_y, scale=60, color="#76c7ff"):
    """Рисуем график с более плавной кривой и другой толщиной линии."""
    prev = None
    width, height = int(cnv["width"]), int(cnv["height"])

    for scr_x in range(width):
        x_val = (scr_x - origin_x) / scale
        try:
            y_val = func(x_val)
            scr_y = origin_y - y_val * scale
        except Exception:
            prev = None
            continue

        if 0 <= scr_y <= height:
            if prev:
                cnv.create_line(prev[0], prev[1], scr_x, scr_y, fill=color, width=3, smooth=True)
            prev = (scr_x, scr_y)
        else:
            prev = None


def bisection_root(f, a, b, eps=1e-5):
    """Находим корень методом бисекции с повышенной точностью."""
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        return None

    while (b - a) / 2 > eps:
        mid = (a + b) / 2
        fmid = f(mid)
        if fmid == 0:
            return mid
        elif fa * fmid < 0:
            b, fb = mid, fmid
        else:
            a, fa = mid, fmid
    return (a + b) / 2


def mark_root(cnv, root_x, ox, oy, scale=60, color="#ff4c4c"):
    """Отмечаем корень красным кругом и подписью с тенью."""
    cx = ox + root_x * scale
    cy = oy
    r = 7
    # Тень
    cnv.create_oval(cx - r + 2, cy - r + 2, cx + r + 2, cy + r + 2, fill="#800000", outline="")
    # Круг
    cnv.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, outline="")
    # Текст с тенью
    cnv.create_text(cx + 1, cy - 16 + 1, text=f"{root_x:.4f}", fill="#440000", font=("Helvetica", 12, "bold"))
    cnv.create_text(cx, cy - 16, text=f"{root_x:.4f}", fill=color, font=("Helvetica", 12, "bold"))


def draw_formula(cnv, ox, oy):
    """Пишем формулу функции в окне."""
    formula_text = "y = -x² + 2"
    cnv.create_text(ox + 300, oy - 270, text=formula_text, fill="#fff", font=("Helvetica", 18, "bold italic"))


def main():
    root = tk.Tk()
    root.title("График функции")
    root.configure(bg="#121421")

    canvas = make_canvas(root)
    origin_x, origin_y = 450, 325
    grid_step = 60

    draw_axes_and_grid(canvas, origin_x, origin_y, step=grid_step)
    draw_formula(canvas, origin_x, origin_y)

    f = lambda x: -x**2 + 2
    plot_function(canvas, f, origin_x, origin_y, scale=grid_step)

    root_x = bisection_root(f, -2.5, 2.5)
    if root_x is not None:
        mark_root(canvas, root_x, origin_x, origin_y, scale=grid_step)
        print(f"Корень функции: x = {root_x:.5f}")

    y_at_zero = f(0)
    print(f"Пересечение с осью Y: (0, {y_at_zero})")

    root.mainloop()


if __name__ == "__main__":
    main()
