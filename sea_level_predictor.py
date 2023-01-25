import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df1 = pd.read_csv('epa-sea-level.csv')
  
    # Create scatter plot
    fig = plt.figure()
    plt.scatter(data=df1,y='CSIRO Adjusted Sea Level',x='Year')
  
    # Create first line of best fit
    res1 = linregress(x=df1.Year, y=df1['CSIRO Adjusted Sea Level'])
    years1 = np.arange(df1.Year.min(),2051,1)
    fit1 = res1.slope*years1 + res1.intercept
    plt.plot(years1, fit1, c='red')

    # Create second line of best fit
    df2 = df1[df1.Year >= 2000]
    res2 = linregress(x=df2.Year, y=df2['CSIRO Adjusted Sea Level'])
    years2 = np.arange(df2.Year.min(),2051,1)
    fit2 = res2.slope*years2 + res2.intercept
    plt.plot(years2, fit2, c='orange')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()