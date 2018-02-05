import barbershop
import numpy as np
import matplotlib.pyplot as plt
import ClosePlots as cp

x = np.linspace(0,10,1000)
y = np.linspace(0,10,1000)
z = np.linspace(0,10,1000)

barber = barbershop.initialize(x, y, 'x', 'y')
barber.histograms_on(x=True,y=True)
barber.add_client(z, 'z', lower=2., upper=8.)
# barber.add_client(z*20000, 'n', lower=30000., upper=90000.)
# barber.add_client(z, 'a')
# barber.add_client(z, 'b')
# barber.add_client(z, 'c')

barber.show_mirror()
cp.show()
