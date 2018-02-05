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
barber.add_client(z*200, 'n', lower=300., upper=900.)

barber.show_mirror()
cp.show()
