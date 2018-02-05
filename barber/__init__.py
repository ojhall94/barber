#!/bin/env python
# -*- coding: utf-8 -*-

"""
A Python package that aids the user in making dynamic cuts to data in various
parameter spaces, using a simple GUI.

.. versioncreated:: 0.1

.. codeauthor:: Oliver James Hall <ojh251@student.bham.ac.uk>
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.widgets import Slider, Button
import glob as glob
import pandas as pd

class initialize:
    def __init__(self, _X, _Y):
        '''
        A class that initialises the barbershop class which all other content is
        appended to.

        Parameters:
            _X (ndarray): The uncut X values to be used to illustrate the data.
            _Y (ndarray): The uncut Y values to be used to illustrate the data.
        '''
        self.X = _X
        self.Y = _Y

        #Check X and Y are of equal length
        if len(X) != len(Y):
            print('X and Y are not of equal length!')
            self.evict_shop()
            print('Please re-initialise barber.')
            return None

        #Premeptively turn both histograms off
        self.hist_x_on = False
        self.hist_y_on = False

        #Initializing other metadata
        self.clients = 0
        self.seating = pd.DataFrame()

    def histograms_on(self,x=False,y=False):
        '''Turn on optional histograms for x and y parameter spaces.
        Parameters:
            x (bool): Default False. Set True to display histogram in x.
            y (bool): Default False. Set True to display histogram in y.
        '''
        self.hist_x_on = x
        self.hist_y_on = y

    def add_client(self, client, lower=-np.inf, upper=np.inf):
        '''
        A class that allows the user to add a parameter to make cuts in, up to
        a maximum of five. The user has the option of setting lower and upper
        limits on the cuts in this parameter space. If values are given for either
        'lower', 'upper', or 'both', these are used to make initial cuts to the
        data.

        Parameters:
            client (ndarray): an array as the same length as self.X and self.Y,
                arranged identically, with parameter values for each data point.

            lower (float): Default -Inf. The lowest possible value of the cut
                in this parameter space. If no value is given, it takes the
                minimum value in the 'client' ndarray.

            upper (float): Default Inf. The highest possible value of the cut
                in this parameter space. If no value is given, it takes the
                highest value in the 'client' ndarray.
        '''
        #Check length of the client is in agreement with X and Y
        if len(client) != len(self.X)
