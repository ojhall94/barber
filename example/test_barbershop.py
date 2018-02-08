import numpy as np
import barbershop
import pandas as pd
import glob

if __name__ == "__main__":
    sfile = glob.glob('GAIA/Repo_Data/*all*.txt')[0]
    df = pd.read_csv(sfile, sep='\s+')
    print(df.info())

    odf = df[df.stage==4]
    colstokeep = ['logAge', '[M/H]', 'logL', 'logTe', 'logg', 'Mact']
    odf[colstokeep].to_csv('example_data.csv')
    sys.exit()
    #Loading in only data classified as Core Helium Burning
    barber = barbershop.open(df[df.stage==4], 'logTe', 'logL')

    #I want to investigate the mass data
    barber.add_client('stage')
    barber.add_client('Mact')

    #I want to make the same cuts
    barber.get_regular('cuts.csv')

    #I want to save out the files as:
    barber.give_savelocs()

    #I want to see how this affects the population in logTe
    barber.histograms_on(x=True, y=True)
    barber.show_mirror()
