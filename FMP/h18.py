from tkinter import *
import math


class GraphApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Функциональный график")
        self.master.geometry("850x620")
        self.master.resizable(False, False)
        self.master.configure(bg="#f5f2e7")

        # Настройки графика
        self.grid_zoom = 60
        self.shift_x = 0
        self.shift_y = 0
        self.free_draw = False
        self.previous = None

        # Для перемещения графика мышкой
        self.is_panning = False
        self.pan_start = None

        self.allowed = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "sqrt": math.sqrt,
            "e": math.e,
            "pi": math.pi,
        }

        self.build_ui()
        self.set_bindings()

    def build_ui(self):
        # Левая панель управления — бежево-кремовая
        self.sidebar = Frame(self.master, width=300, bg="#e6dfd3")
        self.sidebar.pack(side=LEFT, fill=Y)

        Label(
            self.sidebar,
            text="Введите функцию:",
            bg="#d7cdb8",  # теплый бежевый
            fg="#4a432f",  # тёмно-коричневый текст
            wraplength=280,
            justify=LEFT,
            font=("Courier", 11, "bold"),
        ).pack(pady=(20, 8), padx=15)

        self.input = Entry(self.sidebar, font=("Courier", 13), bg="#f0ead8", fg="#4a432f", insertbackground="#4a432f")
        self.input.pack(padx=15, pady=(0, 12), fill=X)

        # Стиль кнопок
        btn_bg = "#d1c3a0"  # светло-бежевый
        btn_active = "#b8a66d"  # темнее при наведении/нажатии
        btn_fg = "#3e3520"  # тёмно-коричневый текст

        def style_button(btn):
            btn.config(
                bg=btn_bg,
                fg=btn_fg,
                font=("Courier", 11),
                relief=FLAT,
                bd=0,
                activebackground=btn_active,
                activeforeground=btn_fg,
                highlightthickness=0,
                padx=10,
                pady=5,
            )

        btn_build = Button(self.sidebar, text="Построить", command=self.render_graph)
        style_button(btn_build)
        btn_build.pack(pady=8, padx=15, fill=X)

        btn_draw = Button(self.sidebar, text="Свободное рисование", command=self.toggle_drawing_mode)
        style_button(btn_draw)
        btn_draw.pack(pady=8, padx=15, fill=X)

        Label(
            self.sidebar,
            text="Масштаб:",
            bg="#d7cdb8",
            fg="#4a432f",
            font=("Courier", 11, "bold"),
        ).pack(pady=(25, 6), padx=15)

        self.zoom_slider = Scale(
            self.sidebar,
            from_=20,
            to=150,
            orient=HORIZONTAL,
            bg="#e6dfd3",
            fg="#4a432f",
            troughcolor="#c9b89a",
            command=self.set_zoom,
            font=("Courier", 9),
            highlightthickness=0,
            sliderrelief=FLAT,
        )
        self.zoom_slider.set(self.grid_zoom)
        self.zoom_slider.pack(pady=(0, 20), padx=15, fill=X)

        nav_frame = Frame(self.sidebar, bg="#e6dfd3")
        nav_frame.pack(pady=15)

        btn_opts = dict(
            width=5,
            bg=btn_bg,
            fg=btn_fg,
            font=("Courier", 12),
            relief=FLAT,
            bd=0,
            activebackground=btn_active,
            activeforeground=btn_fg,
            highlightthickness=0,
            pady=5,
        )
        Button(nav_frame, text="↑", command=lambda: self.shift("up"), **btn_opts).grid(row=0, column=1)
        Button(nav_frame, text="←", command=lambda: self.shift("left"), **btn_opts).grid(row=1, column=0)
        Button(nav_frame, text="→", command=lambda: self.shift("right"), **btn_opts).grid(row=1, column=2)
        Button(nav_frame, text="↓", command=lambda: self.shift("down"), **btn_opts).grid(row=2, column=1)

        # Основное полотно для рисования
        self.canvas = Canvas(self.master, bg="#f8f6f0", highlightthickness=0)
        self.canvas.pack(side=RIGHT, fill=BOTH, expand=True)

    def set_bindings(self):
        self.canvas.bind("<Button-1>", self.begin_draw)
        self.canvas.bind("<B1-Motion>", self.keep_drawing)

        # Перемещение графика мышью левой кнопкой (за исключением режима свободного рисования)
        self.canvas.bind("<ButtonPress-1>", self.start_pan)
        self.canvas.bind("<B1-Motion>", self.do_pan)
        self.canvas.bind("<ButtonRelease-1>", self.end_pan)

    def start_pan(self, event):
        # Режим рисования
        if self.free_draw:
            return
        self.is_panning = True
        self.pan_start = (event.x, event.y)

    def do_pan(self, event):
        if self.is_panning and self.pan_start and not self.free_draw:
            dx = event.x - self.pan_start[0]
            dy = event.y - self.pan_start[1]
            self.shift_x += dx
            self.shift_y += dy
            self.pan_start = (event.x, event.y)
            self.render_graph()

    def end_pan(self, event):
        self.is_panning = False
        self.pan_start = None

    def set_zoom(self, value):
        self.grid_zoom = int(value)
        self.render_graph()

    def toggle_drawing_mode(self):
        self.free_draw = not self.free_draw
        if self.free_draw:
            self.master.config(cursor="pencil")
        else:
            self.master.config(cursor="")

    def begin_draw(self, event):
        if self.free_draw:
            self.previous = (event.x, event.y)

    def keep_drawing(self, event):
        if self.free_draw and self.previous:
            x0, y0 = self.previous
            x1, y1 = event.x, event.y
            self.canvas.create_line(x0, y0, x1, y1, fill="#b85c38", width=2, smooth=True)  # коричнево-терракотовый
            self.previous = (x1, y1)

    def shift(self, direction):
        delta = 25
        if direction == "left":
            self.shift_x += delta
        elif direction == "right":
            self.shift_x -= delta
        elif direction == "up":
            self.shift_y += delta
        elif direction == "down":
            self.shift_y -= delta
        self.render_graph()

    def render_graph(self):
        self.canvas.delete("all")
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        cx, cy = w // 2 + self.shift_x, h // 2 + self.shift_y

        # Оси — мягкий тёмно-бежевый
        self.canvas.create_line(0, cy, w, cy, fill="#8c7a5a", width=2)
        self.canvas.create_line(cx, 0, cx, h, fill="#8c7a5a", width=2)

        # Сетка — светло-бежевый
        step = self.grid_zoom
        if step < 1:
            step = 1
        for i in range(0, w, step):
            self.canvas.create_line(i, 0, i, h, fill="#dcd6c9")
            val = (i - cx) / step
            if abs(val) > 0.01:
                self.canvas.create_text(i, cy + 18, text=f"{val:.0f}", fill="#8c7a5a", font=("Courier", 8))

        for j in range(0, h, step):
            self.canvas.create_line(0, j, w, j, fill="#dcd6c9")
            val = (cy - j) / step
            if abs(val) > 0.01:
                self.canvas.create_text(cx + 25, j, text=f"{val:.0f}", fill="#8c7a5a", font=("Courier", 8))

        # График — тёмно-терракотовый
        expr = self.input.get()
        prev = None
        for px in range(w):
            x = (px - cx) / self.grid_zoom
            try:
                y = eval(expr, {"x": x, "math": math, **self.allowed})
                py = cy - y * self.grid_zoom
                if prev and 0 <= py <= h:
                    self.canvas.create_line(prev[0], prev[1], px, py, fill="#b85c38", width=2, smooth=True)
                prev = (px, py)
            except Exception:
                prev = None


if __name__ == "__main__":
    root = Tk()
    app = GraphApp(root)
    root.mainloop()
