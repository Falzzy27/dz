import tkinter as tk
import math

def f(x):
    return math.tan(x)

def simpson_method(func, start, end, steps):
    if steps % 2 != 0:
        steps += 1  # Метод Симпсона требует чётного числа шагов

    h = (end - start) / steps
    total = func(start) + func(end)
    for i in range(1, steps):
        x = start + i * h
        coeff = 4 if i % 2 != 0 else 2
        try:
            total += coeff * func(x)
        except Exception:
            pass
    return (h / 3) * total

def draw_axes_and_grid(canvas, cx, cy, scale, width=1000, height=800):
    step_grid = 1
    range_grid = 15
    canvas.delete("grid")
    for i in range(-range_grid, range_grid + 1):
        x = cx + i * scale * step_grid
        y = cy - i * scale * step_grid
        canvas.create_line(x, 0, x, height, fill="#e0e0e0", tags="grid")
        canvas.create_line(0, y, width, y, fill="#e0e0e0", tags="grid")
    canvas.create_line(0, cy, width, cy, arrow=tk.LAST, fill="#333", width=2, tags="grid")
    canvas.create_line(cx, 0, cx, height, arrow=tk.LAST, fill="#333", width=2, tags="grid")
    font_small = ("Segoe UI", 9)
    for i in range(-range_grid, range_grid + 1):
        x = cx + i * scale * step_grid
        y = cy - i * scale * step_grid
        canvas.create_line(x, cy - 8, x, cy + 8, fill="#666", width=1.2, tags="grid")
        if i != 0:
            canvas.create_text(x, cy + 22, text=str(i * step_grid), fill="#555", font=font_small, tags="grid")
        canvas.create_line(cx - 8, y, cx + 8, y, fill="#666", width=1.2, tags="grid")
        if i != 0:
            canvas.create_text(cx + 25, y, text=str(i * step_grid), fill="#555", font=font_small, tags="grid")

def draw_function(canvas, func, start, end, cx, cy, scale, step=0.005, color="#1e90ff"):
    canvas.delete("func")
    x = start
    prev_point = None
    while x <= end:
        try:
            y_val = func(x)
        except Exception:
            prev_point = None
            x += step
            continue
        sx = cx + x * scale
        sy = cy - y_val * scale
        if prev_point:
            canvas.create_line(prev_point[0], prev_point[1], sx, sy, fill=color, width=3, smooth=True, tags="func")
        prev_point = (sx, sy)
        x += step

def draw_simpson_visual(canvas, func, start, end, steps, cx, cy, scale, color="#32cd32"):
    canvas.delete("rects")
    if steps % 2 != 0:
        steps += 1
    h = (end - start) / steps
    for i in range(0, steps, 2):
        x0 = start + i * h
        x1 = x0 + h
        x2 = x0 + 2 * h
        try:
            y0 = func(x0)
            y1 = func(x1)
            y2 = func(x2)
        except Exception:
            continue
        for j in range(11):
            t = j / 10
            xt = x0 + 2 * h * t
            yt = (1 - t) * (1 - 2 * t) * y0 + 4 * t * (1 - t) * y1 + t * (2 * t - 1) * y2
            if j > 0:
                canvas.create_line(px, py, cx + xt * scale, cy - yt * scale, fill=color, width=2, tags="rects")
            px = cx + xt * scale
            py = cy - yt * scale

def redraw():
    canvas.delete("all")
    draw_axes_and_grid(canvas, center_x, center_y, scale)
    draw_function(canvas, f, graph_start, graph_end, center_x, center_y, scale)
    if integration_active:
        draw_simpson_visual(canvas, f, a, b, n, center_x, center_y, scale)

def run_integration():
    global integration_active
    try:
        a_val = float(entry_a.get())
        b_val = float(entry_b.get())
        if a_val == b_val:
            raise ValueError("Диапазон интегрирования не может быть нулевым")
    except Exception as e:
        result_label.config(text=f"Ошибка в интервале интегрирования: {e}")
        return

    global a, b, n
    a, b = sorted([a_val, b_val])
    n = max(10, int(abs(b - a) * 50))
    if n % 2 != 0:
        n += 1

    integration_active = True
    redraw()
    result = simpson_method(f, a, b, n)
    result_label.config(text=f"Метод Симпсона: {result:.6f}")

def start_pan(event):
    global pan_start_x, pan_start_y
    pan_start_x = event.x
    pan_start_y = event.y

def do_pan(event):
    global center_x, center_y, pan_start_x, pan_start_y
    dx = event.x - pan_start_x
    dy = event.y - pan_start_y
    center_x += dx
    center_y += dy
    pan_start_x = event.x
    pan_start_y = event.y
    redraw()

def zoom(event):
    global scale, center_x, center_y
    mouse_x, mouse_y = event.x, event.y
    mouse_fx = (mouse_x - center_x) / scale
    mouse_fy = (center_y - mouse_y) / scale
    factor = 1.1 if event.delta > 0 else 1 / 1.1
    new_scale = scale * factor
    if new_scale < 30:
        new_scale = 30
    elif new_scale > 1000:
        new_scale = 1000
    scale = new_scale
    center_x = mouse_x - mouse_fx * scale
    center_y = mouse_y + mouse_fy * scale
    redraw()

# --- Параметры ---
a, b = 0, 1
n = 30
scale = 150
center_x, center_y = 500, 400
integration_active = True
graph_start, graph_end = -5, 5

pan_start_x = None
pan_start_y = None

root = tk.Tk()
root.title("Метод Симпсона — интегрирование")
root.geometry("1000x900")
root.configure(bg="#f5f7fa")
root.resizable(False, False)

canvas = tk.Canvas(root, width=1000, height=700, bg="white", highlightthickness=0)
canvas.pack(pady=15)

interval_frame = tk.Frame(root, bg="#f5f7fa")
interval_frame.pack(pady=10)

tk.Label(interval_frame, text="a =", bg="#f5f7fa", font=("Segoe UI", 11)).pack(side=tk.LEFT)
entry_a = tk.Entry(interval_frame, width=10, font=("Segoe UI", 11))
entry_a.pack(side=tk.LEFT, padx=5)
entry_a.insert(0, str(a))

tk.Label(interval_frame, text="b =", bg="#f5f7fa", font=("Segoe UI", 11)).pack(side=tk.LEFT)
entry_b = tk.Entry(interval_frame, width=10, font=("Segoe UI", 11))
entry_b.pack(side=tk.LEFT, padx=5)
entry_b.insert(0, str(b))

apply_button = tk.Button(interval_frame, text="Вычислить", bg="#6a9fb5", fg="white",
                         font=("Segoe UI", 11, "bold"), relief=tk.FLAT,
                         command=run_integration)
apply_button.pack(side=tk.LEFT, padx=15)

result_label = tk.Label(root, text="Метод Симпсона: ", font=("Segoe UI", 15, "bold"), bg="#f5f7fa", fg="#333")
result_label.pack(pady=15)

canvas.bind("<ButtonPress-1>", start_pan)
canvas.bind("<B1-Motion>", do_pan)
canvas.bind("<MouseWheel>", zoom)
canvas.bind("<Button-4>", lambda e: zoom(type("Event", (), {"x": e.x, "y": e.y, "delta": 120})()))
canvas.bind("<Button-5>", lambda e: zoom(type("Event", (), {"x": e.x, "y": e.y, "delta": -120})()))

run_integration()

root.mainloop()
