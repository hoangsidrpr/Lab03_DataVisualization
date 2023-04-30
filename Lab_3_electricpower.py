# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""
# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('household_power_consumption\\household_power_consumption.txt',
                   delimiter=';', low_memory=False)

############################## Your code for loading and preprocess the data ##
data.Date = pd.to_datetime(data.Date, dayfirst=True)
data = data.loc[data.Date.between('2007-02-01', '2007-02-02')]

data['Global_active_power'] = data['Global_active_power'].astype(float)
data['Sub_metering_1'] = data['Sub_metering_1'].astype(float)
data['Sub_metering_2'] = data['Sub_metering_2'].astype(float)
data['Sub_metering_3'] = data['Sub_metering_3'].astype(float)
data['Voltage'] = data['Voltage'].astype(float)
data['Global_reactive_power'] = data['Global_reactive_power'].astype(float)

# Add date vao time de plot cac chart su dung thoi gian
data['DateTime'] =\
    data['Date'].astype(str) + ' ' + data['Time'].astype(str)
data['DateTime'] = pd.to_datetime(
    data['DateTime'], format='%Y-%m-%d %H:%M:%S')

############################ Complete the following 4 functions ###############

# %%


def plot1():
    plt.hist(data['Global_active_power'], color='red', ec='black', bins=15)
    plt.title('Global Active Power')
    plt.xlabel('Global Active Power (kilowatts)')
    plt.ylabel('Frequency')

    ax = plt.subplot(111)
    ax.set_xbound(min(data['Global_active_power']))
    ax.set_xmargin(min(data['Global_active_power']))
    ax.set_ybound(-50, 1400)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.tight_layout()
    plt.savefig('plot1.png', bbox_inches='tight', dpi=300)
    plt.show()


plot1()

# %%


def plot2(save=False):
    data[['Global_active_power', 'DateTime']].plot(
        x='DateTime', y='Global_active_power',
        color='black', linewidth=0.5)
    plt.ylabel('Global Active Power (kilowatts)')
    plt.tight_layout()
    plt.legend().set_visible(False)

    if save:
        plt.savefig('plot2.png', bbox_inches='tight', dpi=300)


plot2(save=True)

# %%


def plot3(save=False):
    data[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3', 'DateTime']].plot(
        x='DateTime', y=['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'],
        color=['black', 'red', 'blue'], linewidth=0.5)
    plt.ylabel('Energy sub metering')
    plt.tight_layout()

    if save:
        plt.savefig('plot3.png', bbox_inches='tight', dpi=300)


plot3(save=True)

# %%


def plot(column, ax, color='black', ytitle=None):
    if ytitle == None:
        ytitle = column

    ax.plot(
        data['DateTime'], data[column],
        color=color, linewidth=0.5
    )

    ax.set_ylabel(ytitle)
    ax.set_xticks(
        [
            '2007-02-01 00:00:00',
            '2007-02-01 12:00:00',
            '2007-02-02 00:00:00',
            '2007-02-02 12:00:00',
            '2007-02-02 23:59:00'
        ],
        [
            '00:00\n01-Feb\n2007',
            '12:00',
            '00:00\n02-Feb',
            '12:00',
            '23:59',
        ]
    )
    # ax.set_title(f'{column} over time')


def plot4(save=False):
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

    plot('Global_active_power', axs[0, 0],
         ytitle='Global Active Power (kilowatts)')
    
    plot('Voltage', axs[0, 1])
    
    plot('Sub_metering_1', axs[1, 0])
    plot('Sub_metering_2', axs[1, 0], 'red')
    plot('Sub_metering_3', axs[1, 0], 'blue', ytitle='Energy sub metering')
    axs[1, 0].legend(['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'])

    plot('Global_reactive_power', axs[1, 1])

    fig.subplots_adjust(hspace=0.3, wspace=0.3)
    if save:
        fig.savefig('plot4.png', bbox_inches='tight', dpi=500)

    plt.show()


plot4(True)

# %%
