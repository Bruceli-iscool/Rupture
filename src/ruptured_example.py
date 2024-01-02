from src.Ruptured import Ruptured

rp = Ruptured()
x = rp.ask('What\'s your age?')
rp.convert(x, int)
rp.write(x)

