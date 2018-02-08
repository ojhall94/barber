import numpy as np
import barbershop
import pandas as pd
import glob

'''
This code gives an example of all the functionality in the barbershop package,
using an example file of a TRILEGAL simulation (Girardi et al. 2012) of Core
Helium Burning Red Giant stars.

barbershop can be run from a Python file as per this example, but is also optimised
for use in line-by-line compilers such as iPython, and certain functions (such as
check_seating()) are designed specifically for this purpose.

The code will, in this order:
-Load in the data

-Initiate the barbershop module using the data using logTe on the x axis and
    logL on the y axis

-Add the 'client' Mact to allow for cuts in Mass and investigation of trends in Mass.
    I initiate a lower and upper initial cut for Mass, which is optional.

-Add the 'client' [M/H] to allow for cuts in metallicity and investigation of trends
    in metallicity.

-Add the 'client' logg to allow for cuts in logg and investigation of trends in logg.

-REMOVE the 'client' logg to illustrate the programs functionality

-Define the location the data & cuts should be saved out in [Feel free to customize]

-Turn on histograms for logTe and logL

-Display the number of 'clients' currently loaded into the module to illustrate the
    programs functionality. The maximum is 5.

-Display the plots, histograms, and slider.

-After playing around with the slider, the user can save out the cuts.

-If the user saves out the cuts, the program will reload the data (for the sake
    of illustration, lets pretend its a different TRILEGAL simulation).

-Apply the get_regular(sfile) command, applying the same cuts to the same parameters
    and displaying the plots. This is especially useful when applying cuts to multiple
    sets of data, i.e. TRILEGAL simulations for various K2 campaigns.

Have fun!

.. codeauthor:: Oliver James Hall <ojh251@student.bham.ac.uk>
'''

if __name__ == "__main__":
    '''I want to investigate the Secondary Red Clump (see: Girardi 2016) in a
    TRILEGAL simulation (Girardi et al. 2012) of Core Helium Burning stars.'''

    '''Reading in the data we want to make cuts to'''
    sfile = glob.glob('example_data.csv')[0]
    df = pd.read_csv(sfile)
    print(df.info())

    '''Initiating the barbershop module using logTe on the x-axis and logL on the y axis'''
    barber = barbershop.open(df, 'logTe', 'logL')

    '''I want to investigate and make cuts to the Mass values
    I know the Secondary Red Clump lies ~1.5 - 2.0 solar masses.
    '''
    barber.add_client('Mact', lower=1.5, upper=2.0)

    '''I want to investigate and make cuts to the metallicity [M/H] values'''
    barber.add_client('[M/H]')

    '''I want to investigate and make cuts to logg values.'''
    barber.add_client('logg')

    '''Actually I've changed my mind, lets remove 'logg'.'''
    barber.evict_client('logg')

    '''Lets define where we want the output to be saved.
    Note: this is not necessary, but recommended. Default values are:
    floc = dataframe_cut.csv | cloc = cuts.csv'''
    barber.give_savelocs(floc='data_after_cuts.csv',cloc='list_of_cuts.csv')

    '''I want to see how this affects the population in logTe and logL'''
    barber.histograms_on(x=True, y=True)

    '''I want to double check how many 'client' parameter spaces I have loaded in'''
    barber.check_seating()

    '''I want to display the plots and make cuts.'''
    barber.show_mirror()

    '''Now that I've saved out some cuts, I want to load in a new file.'''
    df = pd.read_csv(sfile) #We'll pretend for now this is a different file
    print(df.info())

    '''We need to reinitialise the barbershop module for this new file.'''
    barber = barbershop.open(df, 'logTe', 'logL')

    '''We want to make identical cuts. So first lets define the output location,
    and the lets call get_regular.'''
    barber.give_savelocs(floc='data_2_after_cuts.csv', cloc='list_of_cuts_2.csv')
    barber.get_regular('list_of_cuts.csv')

    print('Thanks for trying out barbershop! Have a great day!')
