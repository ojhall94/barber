#!/bin/env python
# -*- coding: utf-8 -*-

"""
A collection of functions to work in conjunction with __init__.open(), used for
the button functions.

.. versioncreated:: 1.0

.. codeauthor:: Oliver James Hall <ojh251@student.bham.ac.uk>
"""

from matplotlib import pyplot as plt

class barbicideclass:
    def __init__(self, _barber):
        self.barber = _barber

    def all(self, event):
        self.barber.a1min.reset()
        self.barber.a1max.reset()
        self.barber.a2min.reset()
        self.barber.a2max.reset()
        self.barber.a3min.reset()
        self.barber.a3max.reset()
        self.barber.a4min.reset()
        self.barber.a4max.reset()
        self.barber.a5min.reset()
        self.barber.a5max.reset()

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
