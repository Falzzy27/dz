import tkinter as tk
import math

# App window initialization
app = tk.Tk()
app.title("Cartesian Viewport")
canvas_width, canvas_height = 1000, 800
stage = tk.Canvas(app, width=canvas_width, height=canvas_height, bg="white")
stage.pack()


def render_ticks(vertical=True, gap=10, origin_x=500, origin_y=400, axis_len=500, color='gray'):
    tick_size = gap // 10 if gap <= 50 else gap // 20
    units = axis_len // (2 * gap)

    for i in range(-units, units + 1):
        if vertical:
            y = origin_y - i * gap
            stage.create_line(origin_x - tick_size, y, origin_x + tick_size, y, fill=color)
            stage.create_text(origin_x - 3 * tick_size, y, text=str(i), fill=color, font=("Arial", 8, "italic"))
        else:
            x = origin_x + i * gap
            stage.create_line(x, origin_y - tick_size, x, origin_y + tick_size, fill=color)
            stage.create_text(x, origin_y + 3 * tick_size, text=str(i), fill=color, font=("Arial", 8, "italic"))


def render_axis(vertical=True, origin_x=500, origin_y=400, axis_len=500, gap=10, color='black'):
    if vertical:
        stage.create_line(origin_x, origin_y - axis_len // 2, origin_x, origin_y + axis_len // 2, arrow='both',
                          fill=color, width=2)
        render_ticks(True, gap, origin_x, origin_y, axis_len, color)
    else:
        stage.create_line(origin_x - axis_len // 2, origin_y, origin_x + axis_len // 2, origin_y, arrow='both',
                          fill=color, width=2)
        render_ticks(False, gap, origin_x, origin_y, axis_len, color)


def setup_cartesian(gap=20, origin_x=500, origin_y=400, color='black'):
    render_axis(True, origin_x, origin_y, 800, gap, color)
    render_axis(False, origin_x, origin_y, 1000, gap, color)


setup_cartesian()


class Shape:
    """Abstract geometric base"""

    def show_info(self):
        info = f"Area: {self.calc_area():.2f} | Perimeter: {self.calc_perimeter():.2f}"
        print(info)


class Box(Shape):
    """Rectangular shape"""

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def calc_area(self):
        return self.w * self.h

    def calc_perimeter(self):
        return 2 * (self.w + self.h)

    def sketch(self, mid_x=750, mid_y=200, gap=20):
        left = mid_x - (self.w * gap) // 2
        top = mid_y - (self.h * gap) // 2
        right = mid_x + (self.w * gap) // 2
        bottom = mid_y + (self.h * gap) // 2
        stage.create_rectangle(left, top, right, bottom, outline='blue', width=2, fill='#add8e6')


class Disk(Shape):
    """Circular shape"""

    def __init__(self, r):
        self.r = r

    def calc_area(self):
        return math.pi * self.r ** 2

    def calc_perimeter(self):
        return 2 * math.pi * self.r

    def sketch(self, mid_x=250, mid_y=200, gap=20):
        radius_scaled = self.r * gap
        stage.create_oval(mid_x - radius_scaled, mid_y - radius_scaled,
                          mid_x + radius_scaled, mid_y + radius_scaled, outline='red', width=2, fill='#f08080')


class Triad(Shape):
    """Triangle defined by sides"""

    def __init__(self, side_a, side_b, side_c):
        self.a = side_a
        self.b = side_b
        self.c = side_c

    def calc_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calc_perimeter(self):
        return self.a + self.b + self.c

    def sketch(self, base_x=250, base_y=600, gap=20):
        x1, y1 = base_x, base_y - self.a * gap
        x2, y2 = base_x - self.b * gap, base_y + self.b * gap
        x3, y3 = base_x + self.c * gap, base_y + self.c * gap
        stage.create_polygon(x1, y1, x2, y2, x3, y3, outline='green', fill='#90ee90', width=2)


# Instantiate and visualize
square = Box(15, 10)
circle = Disk(9)
triangle = Triad(10, 7, 4)

square.show_info()
square.sketch()

circle.show_info()
circle.sketch()

triangle.show_info()
triangle.sketch()

app.mainloop()
