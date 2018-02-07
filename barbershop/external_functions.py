#!/bin/env python
# -*- coding: utf-8 -*-

"""
A collection of functions to work in conjunction with __init__.open(), used for
the button functions.

.. versioncreated:: 1.0

.. codeauthor:: Oliver James Hall <ojh251@student.bham.ac.uk>
"""

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class barbicideclass:
    def __init__(self, _barber):
        self.barber = _barber

    def all(self, event):
        try:
            self.barber.a1min.reset()
            self.barber.a1max.reset()
        except AttributeError:
            pass
        try:
            self.barber.a2min.reset()
            self.barber.a2max.reset()
        except AttributeError:
            pass
        try:
            self.barber.a3min.reset()
            self.barber.a3max.reset()
        except AttributeError:
            pass
        try:
            self.barber.a4min.reset()
            self.barber.a4max.reset()
        except AttributeError:
            pass
        try:
            self.barber.a5min.reset()
            self.barber.a5max.reset()
        except AttributeError:
            pass

    def a1min(self, event):
        self.barber.a1min.reset()

    def a1max(self, event):
        self.barber.a1max.reset()

    def a2min(self, event):
        self.barber.a2min.reset()

    def a2max(self, event):
        self.barber.a2max.reset()

    def a3min(self, event):
        self.barber.a3min.reset()

    def a3max(self, event):
        self.barber.a3max.reset()

    def a4min(self, event):
        self.barber.a4min.reset()

    def a4max(self, event):
        self.barber.a4max.reset()

    def a5min(self, event):
        self.barber.a5min.reset()

    def a5max(self, event):
        self.barber.a5max.reset()

    def plots(self, event):
        plt.close('all')

class haircutclass:
    def __init__(self, _barber):
        self.barber = _barber

    def update(self, val):
        #Define cut dataframes
        lower = pd.DataFrame()
        upper = pd.DataFrame()

        #Append the slider cut values into this local dataframe
        for idx, client in enumerate(list(self.barber.lowers)):
            if (self.barber.clients >= 1) & (idx == 0):
                lower[client] = [self.barber.a1min.val]
                upper[client] = [self.barber.a1max.val]

            if (self.barber.clients >= 2) & (idx == 1):
                lower[client] = [self.barber.a2min.val]
                upper[client] = [self.barber.a2max.val]

            if (self.barber.clients >= 3) & (idx == 2):
                lower[client] = [self.barber.a3min.val]
                upper[client] = [self.barber.a3max.val]

            if (self.barber.clients >= 4) & (idx == 3):
                lower[client] = [self.barber.a4min.val]
                upper[client] = [self.barber.a4max.val]

            if (self.barber.clients == 5) & (idx == 4):
                lower[client] = [self.barber.a5min.val]
                upper[client] = [self.barber.a5max.val]

        #Get new, cut dataset
        dff = self.barber.shave(lower, upper)

        #Prep the data for update
        uu = np.vstack((dff[self.barber.namex].values, dff[self.barber.namey].values))

        #Update all the axes and colourbars
        for idx, client in enumerate(list(self.barber.lowers)):
            self.barber.axes[idx].collections[0].set_offsets(uu.T)
            self.barber.axes[idx].collections[0].set_array(dff[client])
            try:
                self.barber.axes[idx].collections[0].set_clim([np.nanmin(dff[client]),np.nanmax(dff[client])])
            except ValueError:
                pass
            self.barber.figs[idx].canvas.draw_idle()

        # #Update histograms, if they exist
        if any([self.barber.hist_x_on, self.barber.hist_y_on]):
            if not all([self.barber.hist_x_on, self.barber.hist_y_on]):
                #If only one histogram is turned on
                self.barber.Hax.cla()
                if self.hist_x_on:
                    #Plot original line in red
                    self.barber.Hax.hist(\
                        self.barber.shave(self.barber.lowers, self.barber.uppers)[self.barber.namex],\
                        histtype='step', color='r', bins=self.barber.bins, label='Initial Cut')
                    self.barber.Hax.set_ylabel('Counts')
                    self.barber.Hax.set_xlabel(self.barber.namex)
                    #Plot updated histogram with same bins
                    self.barber.Hax.hist(uu[0], histtype='step', color='k', bins=self.barber.bins, label='Post-Cuts')
                else:
                    #Plot original line in red
                    self.barber.Hax.hist(\
                        self.barber.shave(self.barber.lowers, self.barber.uppers)[self.barber.namey],\
                        histtype='step', color='r', bins=self.barber.bins, label='Initial Cut')
                    self.barber.Hax.set_ylabel('Counts')
                    self.barber.Hax.set_xlabel(self.barber.namey)
                    #Plot updated histogram with same bins
                    self.barber.Hax.hist(uu[1], histtype='step', color='k', bins=self.barber.bins, label='Post-Cuts')
                self.barber.Hax.legend(loc='best',fancybox=True)
            else:
                #If both histograms are turned on
                self.barber.Hax[0].cla()
                self.barber.Hax[1].cla()
                #Plot original line in red
                self.barber.Hax[0].hist(\
                    self.barber.shave(self.barber.lowers, self.barber.uppers)[self.barber.namex],\
                    histtype='step', color='r', bins=self.barber.bins, label='Initial Cut')
                self.barber.Hax[1].hist(\
                    self.barber.shave(self.barber.lowers, self.barber.uppers)[self.barber.namey],\
                    histtype='step', color='r', bins=self.barber.bins, label='Initial Cut')
                #Plot updated histograms with same bins
                self.barber.Hax[0].hist(uu[0],\
                        histtype='step', color='k', bins=self.barber.bins)
                self.barber.Hax[1].hist(uu[1],\
                        histtype='step', color='k', bins=self.barber.bins)
                self.barber.Hax[0].set_ylabel('Counts')
                self.barber.Hax[0].set_xlabel(self.barber.namex)
                self.barber.Hax[1].set_ylabel('Counts')
                self.barber.Hax[1].set_xlabel(self.barber.namey)
                self.barber.Hax[0].legend(loc='best', fancybox=True)
                self.barber.Hax[1].legend(loc='best', fancybox=True)

            self.barber.Hfig.suptitle('Histograms of the data. Pre-cuts shown in red.')
            self.barber.Hfig.tight_layout(rect=[0, 0.03, 1, 0.95])

            self.barber.Hfig.canvas.draw_idle()

def histograms(barber, dff):
    
