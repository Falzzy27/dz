import tkinter as tk

def make_canvas(root, width=800, height=600, bg="#222233"):
    canvas = tk.Canvas(root, width=width, height=height, bg=bg, highlightthickness=0)
    canvas.pack(padx=20, pady=20)
    return canvas

def draw_axes_and_grid(cnv, ox, oy, step=50, color="#666666"):
    w, h = int(cnv["width"]), int(cnv["height"])
    # Сетка по X
    for x in range(0, w, step):
        cnv.create_line(x, 0, x, h, fill=color, dash=(3, 5))
        if abs(x - ox) > 3:
            cnv.create_text(x, oy + 15, text=str((x - ox) // step), fill="#ddd")
    # Сетка по Y
    for y in range(0, h, step):
        cnv.create_line(0, y, w, y, fill=color, dash=(3, 5))
        if abs(y - oy) > 3:
            cnv.create_text(ox - 15, y, text=str(-(y - oy) // step), fill="#ddd")

    # Оси
    cnv.create_line(0, oy, w, oy, fill="#fff", width=2)
    cnv.create_line(ox, 0, ox, h, fill="#fff", width=2)

def plot_function(cnv, f, ox, oy, scale=50, color="#4a90e2"):
    w, h = int(cnv["width"]), int(cnv["height"])
    prev_point = None
    for scr_x in range(w):
        x = (scr_x - ox) / scale
        try:
            y = f(x)
            scr_y = oy - y * scale
        except:
            prev_point = None
            continue

        if 0 <= scr_y <= h:
            if prev_point:
                cnv.create_line(prev_point[0], prev_point[1], scr_x, scr_y, fill=color, width=2)
            prev_point = (scr_x, scr_y)
        else:
            prev_point = None

def newton_method_visual(cnv, f, df, x0, ox, oy, scale=50, eps=1e-6, max_iter=15):
    x = x0
    line_length = 200  # длина касательной в пикселях с каждой стороны от точки касания

    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Производная равна нулю, метод остановлен.")
            return None

        # Экранные координаты текущей точки
        cx = ox + x * scale
        cy = oy - fx * scale

        # Рассчитываем вектор касательной линии
        # Касательная: y = f(x0) + f'(x0)*(x - x0)
        # В экранных координатах наклон будет -dfx * scale, потому что Y инвертирован
        # Направляющий вектор касательной на экране: (dx, dy) с длиной line_length
        # dx = line_length по X, dy = -dfx * scale * dx / scale = -dfx * dx
        # Но проще взять нормализованный вектор и масштабировать.

        # Наклон касательной в экранных координатах (производная в «логических» координатах, Y вверх)
        slope = -dfx  # знак минус из-за инверсии Y в экранных координатах

        # Вектор направления касательной (нормируем)
        from math import sqrt
        dx = 1
        dy = slope
        length = sqrt(dx*dx + dy*dy)
        dx /= length
        dy /= length

        # Конечные точки касательной линии с длиной line_length в обе стороны
        x1 = cx - dx * line_length
        y1 = cy - dy * line_length
        x2 = cx + dx * line_length
        y2 = cy + dy * line_length

        # Рисуем касательную
        cnv.create_line(x1, y1, x2, y2, fill="#00ff88", width=2, dash=(1, 1))

        # Следующее приближение
        x_new = x - fx / dfx

        # Проверка сходимости
        if abs(x_new - x) < eps:
            # Отмечаем найденный корень
            cx_new = ox + x_new * scale
            cy_new = oy
            r_root = 7
            cnv.create_oval(cx_new - r_root, cy_new - r_root, cx_new + r_root, cy_new + r_root, fill="#ff4444", outline="")
            return x_new

        x = x_new

    print("Метод Ньютона не сошелся за заданное количество итераций.")
    return None

def mark_root(cnv, x_root, ox, oy, scale=50, color="#ff4444"):
    cx = ox + x_root * scale
    cy = oy
    r = 8
    cnv.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, outline="")
    cnv.create_text(cx, cy - 15, text=f"x = {x_root:.5f}", fill=color, font=("Arial", 12, "bold"))

def main():
    root = tk.Tk()
    root.title("Метод Ньютона с касательными")

    canvas = make_canvas(root)
    origin_x, origin_y = 400, 300
    grid_step = 50

    draw_axes_and_grid(canvas, origin_x, origin_y, step=grid_step)

    # Функция и ее производная
    f = lambda x: -x**2 + 2
    df = lambda x: -2*x

    plot_function(canvas, f, origin_x, origin_y, scale=grid_step)

    initial_guess = 1.5
    root_x = newton_method_visual(canvas, f, df, initial_guess, origin_x, origin_y, scale=grid_step)
    if root_x is not None:
        mark_root(canvas, root_x, origin_x, origin_y, scale=grid_step)
        print(f"Корень найден: x = {root_x:.6f}")
    else:
        print("Корень не найден")

    root.mainloop()

if __name__ == "__main__":
    main()
