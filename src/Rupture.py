import random
import tkinter as tk
from tkinter import messagebox
import turtle


turtle = turtle


class Rupture:
    def __init__(self):
        self.key_bindings = {}
        self.game_running = True

    def write(self, value):
        print(value)

    def ask(self, value):
        user = input(value)
        return user

    def rad(self, value):
        return random.randint(0, value)

    def window_title(self, title):
        self.window.title(title)
        return

    def window_size(self, x, y):
        self.window.geometry(f"{x}x{y}")
        return

    def window_text(self, text):
        text_message = tk.Message(self.window, text=text, width=300)
        text_message.pack(pady=20)

    def window_header(self, hdr):
        text_label = tk.Label(self.window, text=hdr, wraplength=300)
        text_label.pack(pady=20)

    def start(self):
        self.window.mainloop()

    def size(self, value):
        length = len(value)
        return length

    def draw_window(self):
        self.screen = turtle.Screen()
        self.screen

    def create_brush(self):
        self.turtle = turtle.Turtle()
        return

    def brush_left(self, value):
        self.turtle.left(value)
        return

    def brush_right(self, value):
        self.turtle.right(value)
        return

    def brush_forward(self, value):
        self.turtle.forward(value)
        return

    def brush_backward(self, value):
        self.turtle.forward(value)
        return

    def draw_close(self):
        self.screen.exitonclick()

    def color(self, color):
        self.turtle.color(color)
        return

    def draw_speed(self, speed):
        self.turtle.speed(speed)

    def key_bind(self, key, callback):
        self.key_bindings[key] = callback

    def pressed_key(self, event):
        key = event.char.lower()
        if key in self.key_bindings:
            callback = self.key_bindings[key]
            callback()
        else:
            print(f"Unknown key pressed: {key}")

    def window(self):
        self.window = tk.Tk()

    def hide_brush(self):
        self.turtle.hideturtle()

    def set_position(self, x, y):
        self.turtle.goto(x, y)

    def brush_up(self):
        self.turtle.penup()

    def brush_down(self):
        self.turtle.penup()

    def draw_shape(self, shape):
        self.turtle.shape(shape)

    def fill_color(self, color):
        self.turtle.fillcolor(color)

    def draw_dot(self):
        self.turtle.dot()

    def stamp_brush(self):
        self.turtle.stamp()

    def draw_finish(self):
        self.turtle.done()

    def window_background(self, color):
        self.window.configure(background=color)

    def window_button(self, text, command):
        button = tk.Button(self.window, text=text, command=command)
        button.pack(pady=10)
        return button

    def window_entry(self):
        entry = tk.Entry(self.window)
        entry.pack(pady=10)
        return entry

    def window_popup(title, message):
        messagebox.showinfo(title, message)

    def value_type(self, value):
        vt = type(value)
        return vt

    def convert(self, value, contype):
        con = contype(value)
        return con

    def draw_circle(self, radius):
        if self.turtle:
            self.turtle.circle(radius)
        else:
            print('\033Error: Brush not found\033')

    def draw_square(self, side_length):
        if self.turtle:
            for _ in range(4):
                self.turtle.forward(side_length)
                self.turtle.left(90)
        else:
            print('\033Error: Brush not found\033')

    def draw_triangle(self, side_length):
        if self.turtle:
            for _ in range(3):
                self.turtle.forward(side_length)
                self.turtle.left(120)
        else:
            print('\033Error: Brush not found\033')

    def draw_star(self, size):
        if self.turtle:
            for _ in range(5):
                self.turtle.forward(size)
                self.turtle.right(144)
        else:
            print('\033Error: Brush not found\033')

    def brush_barchart(self, data):
        bar_width = 20
        for value in data:
            self.turtle.begin_fill()
            self.turtle.forward(bar_width)
            self.turtle.left(90)
            self.turtle.forward(value)
            self.turtle.left(90)
            self.turtle.forward(bar_width)
            self.turtle.left(90)
            self.turtle.forward(value)
            self.turtle.left(90)
            self.turtle.end_fill()
            self.turtle.forward(bar_width)

    def brush_scatterplot(self, points):
        for x, y in points:
            self.turtle.penup()
            self.turtle.goto(x, y)
            self.turtle.dot(5)

    def brush_linechart(self, values):
        self.turtle.penup()
        x, y = -150, -150
        for value in values:
            self.turtle.goto(x, y)
            self.turtle.pendown()
            self.turtle.goto(x, y + value)
            x += 30

    def brush_clear(self):
        self.turtle.clear()

    def brush_reset(self):
        self.turtle.reset()

    def brush_size(self, size):
        self.turtle.pensize(size)

    def brush_bgcolor(self, color):
        self.screen.bgcolor(color)

    def draw_polygon(self, sides, length):
        if self.turtle:
            angle = 360 / sides
            for _ in range(sides):
                self.turtle.forward(length)
                self.turtle.left(angle)
        else:
            print('\033Error: Brush not found\033')

    def draw_text(self, text, font=("Arial", 12, "normal")):
        if self.turtle:
            self.turtle.write(text, font=font)
        else:
            print('\033Error: Brush not found\033')

    def draw_arc(self, radius, extent):
        if self.turtle:
            self.turtle.circle(radius, extent=extent)
        else:
            print('\033Error: Brush not found\033')

    def draw_rectcolor(self, width, height, color):
        if self.turtle:
            self.turtle.begin_fill()
            self.turtle.color(color)
            for _ in range(2):
                self.turtle.forward(width)
                self.turtle.left(90)
                self.turtle.forward(height)
                self.turtle.left(90)
            self.turtle.end_fill()
        else:
            print('\033Error: Brush not found\033')

    def draw_image(self, filename):
        if self.turtle:
            self.screen.addshape(filename)
            self.turtle.shape(filename)
        else:
            print('\033Error: Brush not found\033')

    def draw_tricolor(self, side_length, color="yellow"):
        if self.turtle:
            self.turtle.begin_fill()
            self.turtle.color(color)
            for _ in range(3):
                self.turtle.forward(side_length)
                self.turtle.left(120)
            self.turtle.end_fill()
        else:
            print('\033Error: Brush not found\033')
