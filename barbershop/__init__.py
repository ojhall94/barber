#!/bin/env python
# -*- coding: utf-8 -*-

"""
A Python package that aids the user in making dynamic cuts to data in various
parameter spaces, using a simple GUI.

.. versioncreated:: 0.1
.. versionchanged:: 0.2

.. codeauthor:: Oliver James Hall <ojh251@student.bham.ac.uk>
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.widgets import Slider, Button
import glob as glob
import pandas as pd

def update(val):
    return None

class initialize:
    def __init__(self, _X, _Y, _namex, _namey):
        '''
        A class that initialises the barbershop class which all other content is
        appended to.

        Parameters:
            _X (ndarray): The uncut X values to be used to illustrate the data.
            _Y (ndarray): The uncut Y values to be used to illustrate the data.
            _namex (str): The name of the X values
            _namey (str): The name of the Y values
        '''
        self.X = _X
        self.Y = _Y
        self.namex = _namex
        self.namey = _namey

        #Premeptively turn both histograms off
        self.hist_x_on = False
        self.hist_y_on = False

        #Initializing other metadata
        self.clients = 0
        self.seating = pd.DataFrame({self.namex: self.X, self.namey : self.Y})
        self.lowers = pd.DataFrame()
        self.uppers = pd.DataFrame()

        #Check X and Y are of equal length
        if len(self.X) != len(self.Y):
            print('X and Y are not of equal length.')
            self.evict_shop()
            return None

        if any(type(word) != str for word in [self.namex, self.namey]):
            print('Please enter "name" as a string.')
            self.evict_shop()
            return None

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
        if not np.isfinite(lower):
            self.lowers[name] = [np.nanmin(client)]
        else:
            self.lowers[name] = [lower]
        if not np.isfinite(upper):
            self.uppers[name] = [np.nanmax(client)]
        else:
            self.uppers[name] = [upper]

        self.clients += 1
        print('Number of seats in use : '+str(self.clients)+'/5.')

        if self.clients == 5:
            print('The barbershop is now full (5 parameter spaces)')
            print('Please evict a client if you wish to add another.')

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
        del self.hist_x_on
        del self.hist_y_on
        del self.clients
        del self.seating
        del self.lowers
        del self.uppers
        del self.namex
        del self.namey

        print('All metadata have been deleted from memory.')
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
        #Make initial cuts
        dff = self.shave(self.lowers, self.uppers)

        #Initialise initial histograms if requested
        if any([self.hist_x_on, self.hist_y_on]):
            self.bins = int(np.sqrt(len(dff)))      #Save out number of bins for histograms
            if not all([self.hist_x_on, self.hist_y_on]):
                #If only one histogram is turned on
                Hfig, Hax = plt.subplots()              #Create the figure
                if self.hist_x_on:
                    Hax.hist(self.seating[self.namex],\
                            histtype='step', color='k', bins=self.bins)
                    Hax.set_ylabel('Counts')
                    Hax.set_xlabel(self.namex)
                else:
                    Hax.hist(self.seating[self.namey],\
                            histtype='step', color='k', bins=self.bins)
                    Hax.set_ylabel('Counts')
                    Hax.set_xlabel(self.namey)

            else:
                Hfig, Hax = plt.subplots(2)              #Create the figure
                Hax[0].hist(self.seating[self.namex],\
                        histtype='step', color='k', bins=self.bins)
                Hax[1].hist(self.seating[self.namey],\
                        histtype='step', color='k', bins=self.bins)
                Hax[0].set_ylabel('Counts')
                Hax[0].set_xlabel(self.namex)
                Hax[1].set_ylabel('Counts')
                Hax[1].set_xlabel(self.namey)

            Hfig.suptitle('Histograms of the data. Pre-cuts shown in red.')
            Hfig.tight_layout(rect=[0, 0.03, 1, 0.95])

        #Initialise all display parameter plots
        cmaps = ['cool','winter','plasma','viridis','nipy_spectral']
        figs, axes = self.get_shells()
        #Create first build of plots
        for idx, client in enumerate(list(self.lowers)):
            ctemp = axes[idx].scatter(dff[self.namex],dff[self.namey],\
                        cmap = cmaps[idx], c=dff[client], s=3)
            figs[idx].colorbar(ctemp, label=client)
            axes[idx].grid()
            axes[idx].set_axisbelow(True)
            axes[idx].set_xlabel(self.namex)
            axes[idx].set_ylabel(self.namey)

        #Initialise sliders
        '''THIS COMPONENT IS ITERATIVE BUT THE GUI IS NOT IDEAL
        TO DO:
            -Add space for buttons
            -Call axes from a seperate function depending on number of clients
        '''
        Sfig, Sax = plt.subplots(2*self.clients, figsize=(10,2*self.clients))
        axcolor = 'white'
        sliders = []
        for idx, client in enumerate(list(self.lowers)):
            #Maximum value in parameter space 'client'
            a1 = Slider(Sax[int(2*idx)], 'Min '+client,\
                            round(np.nanmin(self.seating[client])),\
                            round(np.nanmax(self.seating[client])),\
                            valinit = self.lowers[client][0])
            #Minimum value in parameter space 'client'
            a2 = Slider(Sax[int(2*idx)+1], 'Max '+client,\
                            round(np.nanmin(self.seating[client])),\
                            round(np.nanmax(self.seating[client])),\
                            valinit = self.uppers[client][0])

        a1.on_changed(update)
        a2.on_changed(update)
        #Assign update function to active sliders
        # if self.clients == 1:
        #     sliders[0].on_changed(update)
        #     sliders[1].on_changed(update)
        # if self.clients == 2:
        #     sliders[2].on_changed(update)
        #     sliders[3].on_changed(update)
        # if self.clients == 3:
        #     sliders[4].on_changed(update)
        #     sliders[5].on_changed(update)
        # if self.clients == 4:
        #     sliders[6].on_changed(update)
        #     sliders[7].on_changed(update)
        # if self.clients == 5:
        #     sliders[8].on_changed(update)
        #     sliders[9].on_changed(update)

        return None

    def get_shells(self):
        '''
        Simple class that returns N empty figures where N is the number of
        variables added using the add_client() function.
        '''
        if self.clients == 1:
            f1, a1 = plt.subplots()
            return [f1], [a1]

        if self.clients == 2:
            f1, a1 = plt.subplots()
            f2, a2 = plt.subplots()
            return (f1, f2), (a1, a2)

        if self.clients == 3:
            f1, a1 = plt.subplots()
            f2, a2 = plt.subplots()
            f3, a3 = plt.subplots()
            return (f1, f2, f3), (a1, a2, a3)

        if self.clients == 4:
            f1, a1 = plt.subplots()
            f2, a2 = plt.subplots()
            f3, a3 = plt.subplots()
            f4, a4 = plt.subplots()
            return (f1, f2, f3, f4), (a1, a2, a3, a4)

        if self.clients == 5:
            f1, a1 = plt.subplots()
            f2, a2 = plt.subplots()
            f3, a3 = plt.subplots()
            f4, a4 = plt.subplots()
            f5, a5 = plt.subplots()
            return (f1, f2, f3, f4, f5), (a1, a2, a3, a4, a5)

    def shave(self, lower, upper):
        '''
        A function that takes the full data array 'self.odf' and applies cuts
        according to the values fed in.

        Parameters:
            lower (pandas.core.frame.DataFrame): A pandas Dataframe containing
                the lower boundary of the cut in each parameter space.

            upper (pandas.core.frame.DataFrame): A pandas Dataframe containing
                the upper boundary of the cut in each parameter space.

        Returns:
            pandas.core.frame.DataFrame: A pandas Dataframe containing the now
                cut data for all parameter spaces.

        '''
        dff = self.seating[:]
        #Apply cuts cyclicly for every client
        for client in list(self.lowers):
            dff = dff[dff[client] > lower[client][0]]
            dff = dff[dff[client] < upper[client][0]]
        return dff
