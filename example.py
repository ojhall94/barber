import barbershop
import numpy as np

x = np.linspace(0,10)
y = np.linspace(0,10)
z = np.linspace(0,10)

barber = barbershop.initialize(x, y, 'x', 'y')
barber.histograms_on(x=True)
barber.add_client(z, 'z')
