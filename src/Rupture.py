import random
import tkinter as tk
import turtle as tur

class Rupture:
    def __init__(self):
        self.window = tk.Tk()

    def write(self):
        print(self)

    def ask(self):
        user_input = input(self)
        return user_input

    def ran(self, value):
        return random.randint(0, value)

    def window_title(self, title):
        self.window.title(title)

    def window_size(self, x, y):
        self.window.geometry(f"{x}x{y}")

    def window_text(self, text):
        text_message = tk.Message(self.window, text=text, width=300)
        text_message.pack(pady=20)

    def window_header(self, hdr):
        text_label = tk.Label(self.window, text=hdr, wraplength=300)
        text_label.pack(pady=20)

    def start(self):
        self.window.mainloop()

    def file_open_read(self):
        with open(self, 'r'):
            pass

    def file_open_write(self):
        with open(self, 'w'):
            pass


