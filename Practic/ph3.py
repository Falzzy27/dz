import tkinter as tk


def create_canvas(parent, width=700, height=500, bg="#fff"):
    canvas = tk.Canvas(parent, width=width, height=height, bg=bg, highlightthickness=0)
    canvas.pack(padx=15, pady=15)
    return canvas


def draw_grid(canvas, ox, oy, step=50):
    w, h = int(canvas["width"]), int(canvas["height"])
    for x in range(0, w, step):
        canvas.create_line(x, 0, x, h, fill="#ddd")
        if abs(x - ox) > 3:
            canvas.create_text(x, oy + 15, text=str((x - ox) // step), fill="#999", font=("Arial", 9))
    for y in range(0, h, step):
        canvas.create_line(0, y, w, y, fill="#ddd")
        if abs(y - oy) > 3:
            canvas.create_text(ox - 15, y, text=str(-(y - oy) // step), fill="#999", font=("Arial", 9))
    canvas.create_line(0, oy, w, oy, fill="#f06d06", width=2)  # X
    canvas.create_line(ox, 0, ox, h, fill="#085f63", width=2)  # Y


def plot_graph(canvas, f, ox, oy, scale=50, color="#f5b700"):
    prev = None
    w, h = int(canvas["width"]), int(canvas["height"])
    for px in range(w):
        x = (px - ox) / scale
        try:
            y = f(x)
            py = oy - y * scale
        except:
            prev = None
            continue
        if 0 <= py <= h:
            if prev:
                canvas.create_line(prev[0], prev[1], px, py, fill=color, width=2, smooth=True)
            prev = (px, py)
        else:
            prev = None


def mark_root(canvas, x_root, ox, oy, scale=50, color="#2ecc71"):
    cx = ox + x_root * scale
    cy = oy
    r = 6
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, outline="")
    canvas.create_text(cx, cy - 15, text=f"{x_root:.4f}", fill=color, font=("Arial", 11, "bold"))


def secant_method_visual(canvas, f, x0, x1, ox, oy, scale=50, tol=1e-5, max_iter=20):
    """Реализация метода секущих с визуализацией на canvas"""
    for _ in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1 - fx0) < 1e-14:  # избегаем деления на 0
            print("Деление на ноль, метод остановлен")
            return None

        # Вычисляем новое приближение
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        # Координаты точек на экране
        cx0, cy0 = ox + x0 * scale, oy - fx0 * scale
        cx1, cy1 = ox + x1 * scale, oy - fx1 * scale
        cx2, cy2 = ox + x2 * scale, oy - f(x2) * scale

        # Рисуем секущую (касательную между x0 и x1)
        canvas.create_line(cx0, cy0, cx1, cy1, fill="#00aaff", width=3, dash=(6, 3))

        # Рисуем точки приближений
        r = 5
        canvas.create_oval(cx0 - r, cy0 - r, cx0 + r, cy0 + r, fill="#ff6600", outline="")
        canvas.create_oval(cx1 - r, cy1 - r, cx1 + r, cy1 + r, fill="#ff6600", outline="")

        # Проверка сходимости по x
        if abs(x2 - x1) < tol:
            # Отмечаем корень
            r_root = 7
            canvas.create_oval(cx2 - r_root, cy2 - r_root, cx2 + r_root, cy2 + r_root, fill="#2ecc71", outline="")
            return x2

        x0, x1 = x1, x2

    print("Метод секущих не сошелся")
    return None


def add_footer_label(root, text):
    label = tk.Label(root, text=text, font=("Arial", 12), fg="#444", pady=5)
    label.pack()


def main():
    root = tk.Tk()
    root.title("Метод секущих с визуализацией")
    root.geometry("730x580")
    root.config(bg="#fafafa")

    canvas = create_canvas(root)
    origin_x, origin_y = 350, 250
    step = 50

    draw_grid(canvas, origin_x, origin_y, step)

    f = lambda x: -x ** 2 + 2
    plot_graph(canvas, f, origin_x, origin_y, scale=step)

    # Начальные приближения для метода секущих
    x0, x1 = 0.5, 2.0
    root_x = secant_method_visual(canvas, f, x0, x1, origin_x, origin_y, scale=step)

    footer_text = "Корень не найден"
    if root_x is not None:
        footer_text = f"Корень функции: x = {root_x:.5f}"

    y0 = f(0)
    footer_text += f" | Пересечение с Y: (0, {y0:.3f})"

    add_footer_label(root, footer_text)

    root.mainloop()


if __name__ == "__main__":
    main()
