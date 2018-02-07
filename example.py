import barbershop
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import ClosePlots as cp
import pandas as pd

# x = np.linspace(0,10,1000)
# y = np.linspace(0,10,1000)
# z = np.linspace(0,10,1000)

x = np.arange(10)
y = np.arange(10)
z = np.arange(10)
df = pd.DataFrame({'x':x, 'y':y, 'z':z, 'n':z, 'a':z, 'b':z, 'c':z})

print(df.info())
barber = barbershop.open(df, 'x', 'y')
barber.histograms_on(x=True,y=True)

barber.add_client('z', lower=1., upper=5.)
barber.add_client('n')

barber.give_savelocs('test.csv','testcuts.csv')

barber.show_mirror()

barber.close_shop()
barber = barbershop.open(df, 'x', 'y')
barber.get_regular('testcuts.csv')

del barber
