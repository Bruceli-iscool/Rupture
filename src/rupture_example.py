from src.Rupture import Rupture

rupture_instance = Rupture()
rupture_instance.window()
rupture_instance.window_size(800, 600)
rupture_instance.window_title("My Turtle Window")
rupture_instance.window_background("lightblue")
rupture_instance.draw_window()
rupture_instance.create_brush()
rupture_instance.bind_key('w', rupture_instance.brush_forward)
rupture_instance.bind_key('s', rupture_instance.brush_backward)
rupture_instance.bind_key('a', lambda: rupture_instance.brush_left(30))
rupture_instance.bind_key('d', lambda: rupture_instance.brush_right(30))
rupture_instance.bind_key('h', rupture_instance.hide_brush)

# New tkinter functions
button = rupture_instance.create_button("Click me", lambda: rupture_instance.show_message("Button Clicked", "Hello from the button!"))

entry = rupture_instance.create_entry()
entry.insert(0, "Type here")

rupture_instance.start()
