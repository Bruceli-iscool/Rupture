from Ruptured import Ruptured

rp = Ruptured()
rp.draw_window
rp.create_brush
rp.brush_name('ArtBoard')
def moveup():
    rp.brush_up(20)

def movedown():
    rp.brush_down()

def moveleft():
    rp.brush_left

def moveright():
    rp.brush_right

def clearboard():
    rp.brush_clear

rp.color('black')

rp.brush_key(clearboard, 'c')    
rp.brush_key(moveright, 'd')
rp.brush_key(moveleft, 'a')
rp.brush_key(movedown, 's')
rp.brush_key(moveup, 'w')
rp.draw_close()



