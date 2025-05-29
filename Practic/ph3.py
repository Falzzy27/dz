import tkinter as tk


def create_canvas(parent, width=700, height=500, bg="#fff"):
    """Создаем белый холст с отступами."""
    canvas = tk.Canvas(parent, width=width, height=height, bg=bg, highlightthickness=0)
    canvas.pack(padx=15, pady=15)
    return canvas


def draw_grid(canvas, ox, oy, step=50):
    """Рисуем сетку светло-серую и цветные оси."""
    w, h = int(canvas["width"]), int(canvas["height"])

    for x in range(0, w, step):
        canvas.create_line(x, 0, x, h, fill="#ddd")
        if abs(x - ox) > 3:
            canvas.create_text(x, oy + 15, text=str((x - ox)//step), fill="#999", font=("Arial", 9))

    for y in range(0, h, step):
        canvas.create_line(0, y, w, y, fill="#ddd")
        if abs(y - oy) > 3:
            canvas.create_text(ox - 15, y, text=str(-(y - oy)//step), fill="#999", font=("Arial", 9))

    # Оси цветные и потолще
    canvas.create_line(0, oy, w, oy, fill="#f06d06", width=2)  # X — оранжевый
    canvas.create_line(ox, 0, ox, h, fill="#085f63", width=2)  # Y — бирюзовый


def plot_graph(canvas, f, ox, oy, scale=50, color="#f5b700"):
    """Рисуем желтый график функции."""
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


def find_root(f, a, b, tol=1e-5):
    """Быстрая бисекция для корня."""
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        return None

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            return c
        elif fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a + b) / 2


def mark_root(canvas, x_root, ox, oy, scale=50, color="#2ecc71"):
    """Отмечаем корень зеленым кружком с подписью."""
    cx = ox + x_root * scale
    cy = oy
    r = 6
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, outline="")
    canvas.create_text(cx, cy - 15, text=f"{x_root:.4f}", fill=color, font=("Arial", 11, "bold"))


def add_footer_label(root, text):
    """Добавляем снизу подпись с результатами."""
    label = tk.Label(root, text=text, font=("Arial", 12), fg="#444", pady=5)
    label.pack()


def main():
    root = tk.Tk()
    root.title("График y = -x² + 2")
    root.geometry("730x580")
    root.config(bg="#fafafa")

    canvas = create_canvas(root)
    origin_x, origin_y = 350, 250
    step = 50

    draw_grid(canvas, origin_x, origin_y, step)

    f = lambda x: -x**2 + 2
    plot_graph(canvas, f, origin_x, origin_y, scale=step)

    root_x = find_root(f, 0, 2)  # или (-2, 0)

    footer_text = "Корень не найден"
    if root_x is not None:
        mark_root(canvas, root_x, origin_x, origin_y, scale=step)
        footer_text = f"Корень функции: x = {root_x:.5f}"

    y0 = f(0)
    footer_text += f" | Пересечение с Y: (0, {y0:.3f})"

    add_footer_label(root, footer_text)

    root.mainloop()


if __name__ == "__main__":
    main()
