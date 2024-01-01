from src.Rupture import Rupture

rupture_instance = Rupture()
rupture_instance.draw_window()
rupture_instance.create_brush()
rupture_instance.color('blue')
rupture_instance.brush_forward(2000)
rupture_instance.draw_close()
rupture_instance.start()
