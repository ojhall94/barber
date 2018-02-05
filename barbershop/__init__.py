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
        if len(self.X) != len(self.Y):
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
        self.lowers = pd.DataFrame()
        self.uppers = pd.DataFrame()

    def histograms_on(self,x=False,y=False):
        '''Turn on optional histograms for x and y parameter spaces.
        Parameters:
            x (bool): Default False. Set True to display histogram in x.
            y (bool): Default False. Set True to display histogram in y.
        '''
        self.hist_x_on = x
        self.hist_y_on = y

    def add_client(self, client, name, lower=-np.inf, upper=np.inf):
        '''
        A function that allows the user to add a parameter to make cuts in, up to
        a maximum of five. The user has the option of setting lower and upper
        limits on the cuts in this parameter space. If values are given for either
        'lower', 'upper', or 'both', these are used to make initial cuts to the
        data.

        Parameters:
            client (ndarray): an array as the same length as self.X and self.Y,
                arranged identically, with parameter values for each data point.

            name (str): a string containing the name of the ndarray client,
                which will be referred to in other functions and printed on the
                GUI.

            lower (float): Default -Inf. The lowest possible value of the cut
                in this parameter space. If no value is given, it takes the
                minimum value in the 'client' ndarray.

            upper (float): Default Inf. The highest possible value of the cut
                in this parameter space. If no value is given, it takes the
                highest value in the 'client' ndarray.
        '''
        #Check that the list of clients isn't already full
        if self.clients == 5:
            print('The barbershop is full, please proceed to plot the GUI, or remove clients using the evict_client(name) command.')
            return None

        #Check length of the client is in agreement with X and Y
        if len(client) != len(self.X):
            print('Client is not of equal length with X and Y.')
            print('Client leaving the barbershop.')
            print('Number of seats in use : '+str(self.clients)+'/5.')
            return None

        #Check that name is a string
        if type(name) != str:
            print('Please enter "name" as a string.')
            print('Client leaving the barbershop.')
            print('Number of seats in use : '+str(self.clients)+'/5.')
            return None

        #Adding the data to the existing class dataframe 'self.seating'
        self.seating[name] = client

        #Save the lower and upper values
        if np.isinfinite(lower):
            self.lowers[name] = np.nanmin(client)
        else:
            self.lowers[name] = lower
        if np.isinfinite(upper):
            self.uppers[name] = np.nanmax(client)
        else:
            self.uppers[name] = upper

        self.clients += 1
        print('Number of seats in use : '+str(self.clients)+'/5.')

        if self.clients == 5:
            print('The barbershop is now full (5 sets of parameters')
            print('Please evict a client to add another.')

    def evict_client(self, name):
        '''
        Simple function that allows the user to remove a set of data in a given
        parameter space by passing the name it was given when added to the
        'add_client' function.

        Parameters:
            name (str): a string containing the name of the ndarray client,
                which will be referred to in other functions and printed on the
                GUI.
        '''
        #Check that name is a string
        if type(name) != str:
            print('Please enter "name" as a string.')
            return None

        #Check this name is actually included in the list of clients
        if not any(word == name for word in list(self.seating)):
            print('There is no set of parameters in the list of clients with this name.')
            return None

        #Remove client of title 'name' from the list of parameters
        del self.seating[name]
        del self.lowers[name]
        del self.uppers[name]
        self.clients -= 1

        print('Number of seats in use : '+str(self.clients)+'/5.')

    def evict_shop(self):
        '''
        Simple function that allows the user to reset the barbershop class
        completely by deleting all existing metadata.
        '''
        del self.X
        del self.Y
        print('Please re-initialize the module.')

    def show_mirror(self):
        '''
        A function that plots the data, sliders for cuts, and buttons.
        It plots:
            -For each client: a plot of X vs Y coloured according to the client
                data with corresponding colourbar.
            -A plot of X vs Y
            -(Optional): A histogram in X and/or Y
            -A plot containing up to 10 sliders (two for each client), buttons to
                reset the cuts on each slider, to save out the data, and to close
                all plots.
        '''
        return None
