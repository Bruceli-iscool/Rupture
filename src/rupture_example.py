from src.Rupture import Rupture

rp = Rupture()
x = rp.ask('What\'s your age?')
rp.convert(x, int)
rp.write(x)


