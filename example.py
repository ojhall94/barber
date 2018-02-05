import barbershop
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10)
y = np.linspace(0,10)
z = np.linspace(0,10)

barber = barbershop.initialize(x, y, 'x', 'y')
barber.histograms_on(x=True,y=True)
barber.add_client(z, 'z', lower=2., upper=8.)
barber.add_client(z, 'n', lower=3., upper=9.)

barber.show_mirror()
plt.show()
