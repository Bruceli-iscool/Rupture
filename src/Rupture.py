import random
import tkinter as tk
import turtle

turtle = turtle


class Rupture:
    def __init__(self):
        self.turtle = turtle
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
        self.turtle.Screen()

    def create_brush(self):
        self.turtle.Turtle()
        return

    def brush_left(self, value):
        self.turtle.left(value)
        return

    def brush_right(self, value):
        self.turtle.left(value)
        return

    def brush_forward(self, value):
        self.turtle.right(value)
        return

    def draw_close(self):
        self.turtle.exitonclick()

    def color(self):
        turtle.color(self)

    def draw_speed(self, speed):
        self.turtle.speed(speed)

    def pressed_key(self, event):
        key = event.char.lower()
        if key in self.key_bindings:
            callback = self.key_bindings[key]
            callback()
        else:
            print(f"Unknown key pressed: {key}")

    def window(self):
        self.window = tk.Tk()
