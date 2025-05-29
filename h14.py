import tkinter as tk
import math

# Настройка окна
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800
CENTER_X, CENTER_Y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2

window = tk.Tk()
window.title("График функции")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="white")
canvas.pack()

def draw_ticks(vertical=True, spacing=10, center_x=CENTER_X, center_y=CENTER_Y, axis_len=500, color='black'):
    """Рисует отсечки на координатных осях."""
    tick_size = spacing // 10 if spacing <= 50 else spacing // 20
    canvas_w = int(canvas['width'])
    canvas_h = int(canvas['height'])

    if vertical:
        shift = (canvas_h - axis_len) // 2
        start = center_y - shift
        count_pos = (axis_len - start) // spacing
        count_neg = start // spacing
        for i in range(1, count_pos):
            y = center_y + i * spacing
            canvas.create_line(center_x - tick_size, y, center_x + tick_size, y, fill=color)
            canvas.create_text(center_x + tick_size * 2, y, text=-i, fill=color)
        for i in range(1, count_neg):
            y = center_y - i * spacing
            canvas.create_line(center_x - tick_size, y, center_x + tick_size, y, fill=color)
            canvas.create_text(center_x + tick_size * 2, y, text=i, fill=color)
    else:
        shift = (canvas_w - axis_len) // 2
        start = center_x - shift
        count_pos = (axis_len - start) // spacing
        count_neg = start // spacing
        for i in range(1, count_pos):
            x = center_x + i * spacing
            canvas.create_line(x, center_y - tick_size, x, center_y + tick_size, fill=color)
            canvas.create_text(x, center_y + tick_size * 2, text=i, fill=color)
        for i in range(1, count_neg):
            x = center_x - i * spacing
            canvas.create_line(x, center_y - tick_size, x, center_y + tick_size, fill=color)
            canvas.create_text(x, center_y + tick_size * 2, text=-i, fill=color)

    # Центр
    canvas.create_text(center_x - tick_size * 2, center_y + tick_size * 2, text='0')
    canvas.create_oval(center_x - tick_size, center_y - tick_size,
                       center_x + tick_size, center_y + tick_size, fill=color)

def draw_axis(vertical=True, axis_len=500, center_x=CENTER_X, center_y=CENTER_Y,
              spacing=10, color='black'):
    """Рисует координатную ось и вызывает draw_ticks."""
    if vertical:
        y_shift = (WINDOW_HEIGHT - axis_len) // 2
        canvas.create_line(center_x, y_shift + axis_len, center_x, y_shift, arrow='first', fill=color)
        draw_ticks(True, spacing, center_x, center_y, axis_len, color)
    else:
        x_shift = (WINDOW_WIDTH - axis_len) // 2
        canvas.create_line(x_shift, center_y, x_shift + axis_len, center_y, arrow='last', fill=color)
        draw_ticks(False, spacing, center_x, center_y, axis_len, color)

def setup_axes(show_x=True, show_y=True, spacing=10, center_x=CENTER_X, center_y=CENTER_Y, color='black'):
    """Рисует оси по флагам."""
    if show_y:
        draw_axis(True, 500, center_x, center_y, spacing, color)
    if show_x:
        draw_axis(False, 800, center_x, center_y, spacing, color)

def default_function(x):
    return math.sin(x)

def draw_function(func, x_start, x_end, spacing, center_x, center_y,
                  mark_x=None, color='blue', thickness=2, dot_color='red'):
    """Рисует функцию на интервале и отмечает точку при заданном X."""
    step = 0.1
    points = int((x_end - x_start) / step)

    for i in range(points):
        x0 = (x_start + i * step)
        x1 = x0 + step
        y0 = func(x0)
        y1 = func(x1)

        canvas.create_line(
            center_x + x0 * spacing, center_y - y0 * spacing,
            center_x + x1 * spacing, center_y - y1 * spacing,
            fill=color, width=thickness
        )

    # Отметка точки
    if mark_x is not None:
        y = func(mark_x)
        x_canvas = center_x + mark_x * spacing
        y_canvas = center_y - y * spacing
        tick_size = spacing // 10 if spacing <= 50 else spacing // 20

        # Точка
        canvas.create_oval(x_canvas - tick_size, y_canvas - tick_size,
                           x_canvas + tick_size, y_canvas + tick_size,
                           fill=dot_color)
        canvas.create_text(x_canvas + spacing // tick_size, y_canvas + tick_size * 2,
                           text=f'({mark_x}, {round(y, 2)})', anchor='nw')

# Конфигурация графика
SCALE = 100
LINE_WIDTH = 3

setup_axes(True, True, spacing=SCALE)
draw_function(default_function, -7, 7, spacing=SCALE, center_x=CENTER_X, center_y=CENTER_Y,
              mark_x=2, color='green', dot_color='black', thickness=LINE_WIDTH)

tk.mainloop()
