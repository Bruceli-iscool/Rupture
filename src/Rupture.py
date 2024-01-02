import random
import tkinter as tk
from tkinter import messagebox
import turtle

turtle = turtle


class Rupture:
    def __init__(self):
        self.screen = turtle.Screen()
        self.key_bindings = {}
        self.game_running = True

    def write(self):
        print(self)
        return

    def ask(self):
        user_input = input(self)
        return user_input

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

    def size(self):
        len(self)
        return

    def draw_window(self):
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

    def window_popup(self, title, message):
        messagebox.showinfo(title, message)
