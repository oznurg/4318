#TermProject
#Koray EKICI - 2148922
#Melih SARI - 2220895
#Oznur GUNGOR - 2076396
#Ruhi AKDOĞAN - 2148534

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import Holt 
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.api import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# The following lines are to suppress warning messages.
import warnings
warnings.filterwarnings("ignore")

# Load data into a dataframe object, also create a copy of raw data in an array
original = pd.read_csv('thy.csv', sep=',')
print(original)
dataframe = original.head(len(original)-1)
dataframe.info()
print(dataframe)
name='Adj Close'

freq = 12 #12 months per year
series = dataframe['Adj Close']
print(series)
numbers = np.asarray(series,dtype='int')
result = sm.tsa.seasonal_decompose(numbers,freq=12,model='Additive')

result.plot()
plt.show() 

# Function for Naive
def estimate_naive(df, seriesname):
    numbers = np.asarray ( df[seriesname] )
    return float( numbers[-1] )
    
naive = estimate_naive (dataframe, name)
print ("Naive estimation:", naive)

# Function for Simple Average
def estimate_simple_average(df,seriesname):
    avg = df[seriesname].mean()
    return avg

simpleaverage =  estimate_simple_average(dataframe, name)
print("Simple average estimation:", simpleaverage)

# Function for Moving Average
def estimate_moving_average(df,seriesname,windowsize):
    avg = df[seriesname].rolling(windowsize).mean().iloc[-1]
    return avg

months = 12 # observed period is 12 months
movingaverage = estimate_moving_average(dataframe,name, months)
print("Moving average estimation for last ", months, " months: ", movingaverage)

# Function for Simple Exponential Smoothing
def estimate_ses(df, seriesname, alpha=0.7):
    numbers = np.asarray(df[seriesname])
    estimate = SimpleExpSmoothing(numbers).fit(smoothing_level=alpha,optimized=False).forecast(1)
    return estimate

alpha = 0.7
ses = estimate_ses(dataframe, name, alpha)[0]
print("Exponential smoothing estimation with alpha =", alpha, ": ", ses)

# Trend estimation with Holt
def estimate_holt(df, seriesname, alpha=0.7, slope=0.1):
    numbers = np.asarray(df[seriesname])
    model = Holt(numbers)
    fit = model.fit(alpha,slope)
    estimate = fit.forecast(1)[-1]
    return estimate

alpha = 0.7
slope = 0.1
holt = estimate_holt(dataframe,name,alpha, slope)
print("Holt trend estimation with alpha =", alpha, ", and slope =", slope, ": ", holt)

results = pd.DataFrame({'Method':['Naive', 'Simple Average', 'Moving Average', 'Exponential Smoothing',
        'Holt Trend'], 'Forecast':[naive, simpleaverage, movingaverage, ses,holt]})
print(results)

