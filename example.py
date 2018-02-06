import barbershop
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import ClosePlots as cp

x = np.linspace(0,10,1000)
y = np.linspace(0,10,1000)
z = np.linspace(0,10,1000)

barber = barbershop.open(x, y, 'x', 'y')
barber.histograms_on(x=True,y=True)
barber.add_client(z, 'z', lower=2., upper=8.)
barber.add_client(z*20000, 'n', lower=30000., upper=90000.)
barber.add_client(z, 'a')
barber.add_client(z, 'b')
barber.add_client(z, 'c')


barber.show_mirror()
# def get_slider(barber):
#     # barber.show_mirror()
#     axcolor='white'
#     Sfig, Sax = plt.subplots()
#     Sfig.subplots_adjust(bottom = 0.45)
#     a1 = Sfig.add_axes([0.15, 0.1, 0.60, 0.03], facecolor=axcolor)
#     a2 = Sfig.add_axes([0.15, 0.14, 0.60, 0.03], facecolor=axcolor)
#     a1max = Slider(a1, 'Max', round(np.nanmin(barber.seating['z'])),\
#                                 round(np.nanmax(barber.seating['z'])), valinit=barber.lowers['z'][0])
#     a1min = Slider(a2, 'Max', round(np.nanmin(barber.seating['z'])),\
#                                 round(np.nanmax(barber.seating['z'])), valinit=barber.uppers['z'][0])
#
#     return Sfig, a1, a2
# Sfig, a1, a2 = get_slider(barber)
cp.show()


'''
check_seating
barbiside [reset cuts]?
'''
