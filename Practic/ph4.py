import tkinter as tk
import math

def create_canvas(parent, width=700, height=500, bg="#fff"):
    canvas = tk.Canvas(parent, width=width, height=height, bg=bg, highlightthickness=0)
    canvas.pack(padx=15, pady=15)
    return canvas

def draw_grid(canvas, ox, oy, step=50):
    w, h = int(canvas["width"]), int(canvas["height"])
    for x in range(0, w, step):
        canvas.create_line(x, 0, x, h, fill="#ddd")
        if abs(x - ox) > 3:
            canvas.create_text(x, oy + 15, text=str(round((x - ox) / step, 1)), fill="#999", font=("Arial", 9))
    for y in range(0, h, step):
        canvas.create_line(0, y, w, y, fill="#ddd")
        if abs(y - oy) > 3:
            canvas.create_text(ox - 20, y, text=str(round(-(y - oy) / step, 1)), fill="#999", font=("Arial", 9))
    # оси
    canvas.create_line(0, oy, w, oy, fill="#f06d06", width=2)  # X
    canvas.create_line(ox, 0, ox, h, fill="#085f63", width=2)  # Y

# График
def plot_graph(canvas, f, ox, oy, scale=50, color="#f5b700"):
    prev = None
    w, h = int(canvas["width"]), int(canvas["height"])
    for px in range(w):
        x = (px - ox) / scale
        try:
            y = f(x)
            py = oy - y * scale
        except Exception:
            prev = None
            continue
        if 0 <= py <= h:
            if prev:
                canvas.create_line(prev[0], prev[1], px, py, fill=color, width=2, smooth=True)
            prev = (px, py)
        else:
            prev = None

# Диагональ
def plot_diagonal(canvas, ox, oy, scale=50, color="#999999"):
    w, h = int(canvas["width"]), int(canvas["height"])
    x0_screen = 0
    y0_screen = oy - ((0 - ox)/scale) * scale  # = oy (проверим)
    x1_screen = w
    y1_screen = oy - ((w - ox)/scale) * scale
    canvas.create_line(ox - scale * 5, oy + scale * 5, ox + scale * 5, oy - scale * 5, fill=color, width=2, dash=(5, 3))

def draw_iterations(canvas, xs, g, ox, oy, scale=50, color="#e74c3c"):
    if not xs:
        return
    r = 5
    # Итерации: точки (x_n, g(x_n))
    points = []
    for x in xs:
        try:
            y = g(x)
        except Exception:
            y = 0
        cx = ox + x * scale
        cy = oy - y * scale
        points.append((cx, cy))
    # точки и линии между итерациями
    for i, (cx, cy) in enumerate(points):
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, outline="")
        if i > 0:
            pcx, pcy = points[i - 1]
            canvas.create_line(pcx, pcy, cx, cy, fill=color, width=2)

def simple_iteration(g, x0, tol=1e-6, max_iter=50):
    xs = [x0]
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        xs.append(x_new)
        if abs(x_new - x) < tol:
            break
        x = x_new
    return xs

def main():
    root = tk.Tk()
    root.title("Метод простой итерации")
    root.geometry("730x580")
    root.config(bg="#fafafa")

    canvas = create_canvas(root)
    origin_x, origin_y = 350, 250
    step = 50

    draw_grid(canvas, origin_x, origin_y, step)

    # Функция g(x)
    def g(x):
        return math.cos(x)

    xs = simple_iteration(g, 1.0)

    plot_graph(canvas, g, origin_x, origin_y, scale=step, color="#f5b700")
    plot_diagonal(canvas, origin_x, origin_y, scale=step, color="#999999")
    draw_iterations(canvas, xs, g, origin_x, origin_y, scale=step, color="#e74c3c")

    last_x = xs[-1]
    text = f"Приближение корня: {last_x:.6f}\nИтераций: {len(xs) - 1}"
    label = tk.Label(root, text=text, font=("Arial", 14), bg="#fafafa", fg="#333", pady=10)
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
