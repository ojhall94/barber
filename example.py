import barbershop
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import ClosePlots as cp

# x = np.linspace(0,10,1000)
# y = np.linspace(0,10,1000)
# z = np.linspace(0,10,1000)

x = np.arange(50000)
y = np.arange(50000)
z = np.arange(50000)

barber = barbershop.open(x, y, 'x', 'y')
barber.histograms_on(x=True,y=True)
barber.add_client(z, 'z')
barber.add_client(z, 'n')
barber.add_client(z, 'a')
barber.add_client(z, 'b')
barber.add_client(z, 'c')



barber.show_mirror()


'''
check_seating
barbiside [reset cuts]?
'''
