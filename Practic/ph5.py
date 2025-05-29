import tkinter as tk
import math

def f(x):
    return math.tan(x)

def rectangle_method(func, start, end, steps, mode):
    h = (end - start) / steps
    total = 0
    x = start + (h if mode == 1 else 0)
    for _ in range(steps):
        try:
            total += func(x) * h
        except Exception:
            pass
        x += h
    return total

def trapezoid_method(func, start, end, steps):
    h = (end - start) / steps
    total = 0
    x = start
    for i in range(steps):
        try:
            y1 = func(x)
            y2 = func(x + h)
            if abs(y1) > 1e3 or abs(y2) > 1e3:
                y1 = 0
                y2 = 0
            total += (y1 + y2) * h / 2
        except Exception:
            pass
        x += h
    return total

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

def draw_rectangles(canvas, func, start, end, steps, cx, cy, scale, mode, color="#ffa500"):
    canvas.delete("rects")
    h = (end - start) / steps
    for i in range(steps):
        x_left = start + i * h
        x_right = x_left + h
        x_val = x_left if mode == 0 else x_right
        try:
            y_val = func(x_val)
            if abs(y_val) > 1e3:
                y_val = 0
        except Exception:
            y_val = 0
        x0 = cx + x_left * scale
        x1 = cx + x_right * scale
        y0 = cy
        y1 = cy - y_val * scale
        canvas.create_rectangle(x0, y0, x1, y1, outline=color, fill=color, stipple="gray12", tags="rects")

def draw_trapezoids(canvas, func, start, end, steps, cx, cy, scale, color="#228B22"):
    canvas.delete("rects")
    h = (end - start) / steps
    for i in range(steps):
        x0 = start + i * h
        x1 = x0 + h
        try:
            y0 = func(x0)
            y1 = func(x1)
            if abs(y0) > 1e3 or abs(y1) > 1e3:
                y0 = 0
                y1 = 0
        except Exception:
            y0 = 0
            y1 = 0
        # Координаты для рисования трапеции
        px0 = cx + x0 * scale
        px1 = cx + x1 * scale
        py0 = cy - y0 * scale
        py1 = cy - y1 * scale

        # Рисует трапецию как многоугольник
        canvas.create_polygon(px0, cy, px0, py0, px1, py1, px1, cy,
                              outline=color, fill=color, stipple="gray25", tags="rects")

def redraw():
    canvas.delete("all")
    draw_axes_and_grid(canvas, center_x, center_y, scale)
    draw_function(canvas, f, graph_start, graph_end, center_x, center_y, scale)
    if integration_active:
        if method == "rectangle":
            draw_rectangles(canvas, f, a, b, n, center_x, center_y, scale, mode)
        elif method == "trapezoid":
            draw_trapezoids(canvas, f, a, b, n, center_x, center_y, scale)

def run_integration(new_mode=None, new_method=None):
    global mode, integration_active, method
    if new_mode is not None:
        mode = new_mode
    if new_method is not None:
        method = new_method

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

    integration_active = True
    redraw()

    if method == "rectangle":
        result = rectangle_method(f, a, b, n, mode)
        method_name = "Метод прямоугольников"
    elif method == "trapezoid":
        result = trapezoid_method(f, a, b, n)
        method_name = "Метод трапеций"
    else:
        result = 0
        method_name = "Неизвестный метод"

    result_label.config(text=f"{method_name}: приближённое значение интеграла: {result:.6f}")

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
    factor = new_scale / scale
    scale = new_scale
    center_x = mouse_x - mouse_fx * scale
    center_y = mouse_y + mouse_fy * scale
    redraw()

# --- Параметры ---
a, b = 0, 1
n = 30
scale = 150
center_x, center_y = 500, 400
mode = 0
method = "rectangle"
integration_active = True
graph_start, graph_end = -5, 5

pan_start_x = None
pan_start_y = None

root = tk.Tk()
root.title("Метод прямоугольников и трапеций — интегрирование")
root.geometry("1000x900")
root.configure(bg="#f5f7fa")
root.resizable(False, False)

canvas = tk.Canvas(root, width=1000, height=700, bg="white", highlightthickness=0)
canvas.pack(pady=15)

btn_frame = tk.Frame(root, bg="#f5f7fa")
btn_frame.pack(pady=10)

btn_left = tk.Button(btn_frame, text="Левые прямоугольники", width=20, bg="#ffa500", fg="white",
                     activebackground="#ff8c00", activeforeground="white",
                     relief=tk.FLAT, font=("Segoe UI", 11, "bold"),
                     command=lambda: run_integration(0, "rectangle"))
btn_left.pack(side=tk.LEFT, padx=10)

btn_right = tk.Button(btn_frame, text="Правые прямоугольники", width=20, bg="#ff4500", fg="white",
                      activebackground="#ff6347", activeforeground="white",
                      relief=tk.FLAT, font=("Segoe UI", 11, "bold"),
                      command=lambda: run_integration(1, "rectangle"))
btn_right.pack(side=tk.LEFT, padx=10)

btn_trapezoid = tk.Button(btn_frame, text="Метод трапеций", width=20, bg="#228B22", fg="white",
                          activebackground="#32CD32", activeforeground="white",
                          relief=tk.FLAT, font=("Segoe UI", 11, "bold"),
                          command=lambda: run_integration(None, "trapezoid"))
btn_trapezoid.pack(side=tk.LEFT, padx=10)

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

apply_button = tk.Button(interval_frame, text="Применить", bg="#6a9fb5", fg="white",
                         font=("Segoe UI", 11, "bold"), relief=tk.FLAT,
                         command=lambda: run_integration())
apply_button.pack(side=tk.LEFT, padx=15)

result_label = tk.Label(root, text="Приближённое значение интеграла:", font=("Segoe UI", 15, "bold"), bg="#f5f7fa", fg="#333")
result_label.pack(pady=15)

canvas.bind("<ButtonPress-1>", start_pan)
canvas.bind("<B1-Motion>", do_pan)

canvas.bind("<MouseWheel>", zoom)
canvas.bind("<Button-4>", lambda e: zoom(type("Event", (), {"x": e.x, "y": e.y, "delta": 120})()))
canvas.bind("<Button-5>", lambda e: zoom(type("Event", (), {"x": e.x, "y": e.y, "delta": -120})()))

run_integration(0, "rectangle")

root.mainloop()
