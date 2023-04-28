# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('household_power_consumption\\household_power_consumption.txt',delimiter=';',low_memory=False)
############################## Your code for loading and preprocess the data ##
data.Date = pd.to_datetime(data.Date,dayfirst=True)
data = data.loc[data.Date.between('2007-02-01','2007-02-02')]

data['Global_active_power'] = data['Global_active_power'].astype(float) 

############################ Complete the following 4 functions ###############
def plot1():
    plt.hist(data['Global_active_power'],color = 'red',ec = 'black',bins = 15)
    plt.title('Global Active Power')
    plt.xlabel( 'Global Active Power (kilowatts)')
    plt.ylabel('Frequency')

    ax = plt.subplot(111) 
    ax.set_xbound(min(data['Global_active_power']))
    ax.set_xmargin(min(data['Global_active_power']))
    ax.set_ybound(-50,1400)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
     
    plt.tight_layout()
    plt.savefig('plot1.png', bbox_inches='tight')
    plt.show()

def plot2():
    pass

def plot3():
    pass

def plot4():
    pass

plot1()