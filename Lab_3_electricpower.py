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

## Add date vao time de plot cac chart su dung thoi gian 
data['DateTime']=\
    data['Date'].astype(str) + ' ' + data['Time'].astype(str)
data['DateTime'] = pd.to_datetime(
    data['DateTime'], format='%Y/%m/%d %H:%M:%S')

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
    plt.savefig('plot1.png', bbox_inches='tight')
    plt.show()

plot1()

#%%
def plot2():
    # data[['Global_active_power', 'DateTime']].plot(
    #     x='DateTime', y='Global_active_power', color='black')
    plt.plot(data['DateTime'], data['Global_active_power'], color='black')
    plt.ylabel('Global Active Power (kilowatts)')
    plt.setp(plt.gca().get_lines(), linewidth=0.5)
    plt.tight_layout()
    plt.savefig('plot2.png', bbox_inches='tight')
    # plt.legend().set_visible(False)

    plt.show()

plot2()

# %%
def plot3(ax=None):
    ax=data[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3', 'DateTime']].plot(
        x='DateTime', y=['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'], color=['black', 'red', 'blue'], linewidth=0.5)
    ax.set_ylabel('Energy sub metering')
    # ax.setp(ax.gca().get_lines(), linewidth=0.5)
    # linewidth = 0.5
    
    # ax.tight_layout()
    ax.figure.savefig('plot3.png', bbox_inches='tight')

    # ax.show()

plot3(plt.figure())

# %%
def add_plot(column, save=False):
    data[[column, 'DateTime']].plot(
        x='DateTime', y=column, color='black')
    plt.ylabel(column)
    plt.setp(plt.gca().get_lines(), linewidth=0.5)
    plt.tight_layout()
    plt.legend().set_visible(False)

    if save: plt.savefig(f'{column}.png', bbox_inches='tight')

    plt.show()

add_plot('Voltage').show()
add_plot('Global_reactive_power').show()

# %%
def plot4():
    # add 4 subplots
    # plot_list=[add_plot('Voltage'), add_plot('Voltage'), plot2(), plot3()]
    fig = plt.figure(figsize=(8, 8))

    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(
        data=data[['Global_active_power', 'DateTime']],
        x='DateTime', y='Global_active_power', color='black'
    )


plot4()

# %%
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# axs[0, 0].plot(data['Time'], data['Global_active_power'], color='black')
# axs[0, 0].set_ylabel('Global Active Power (kilowatts)')
plot2()
axs[0, 0].get_children()[0]

plot3()
axs[0, 1].get_children()[0]


# axs[0, 1].plot(data['DateTime'], data['Voltage'], color='black')
# axs[0, 1].set_ylabel('Voltage')

# axs[1, 0].plot(data['DateTime'], data['Sub_metering_1'], color='black')
# axs[1, 0].plot(data['DateTime'], data['Sub_metering_2'], color='red')
# axs[1, 0].plot(data['DateTime'], data['Sub_metering_3'], color='blue')
# axs[1, 0].set_ylabel('Energy sub metering')

# axs[1, 1].plot(data['DateTime'], data['Global_reactive_power'], color='black')
# axs[1, 1].set_ylabel('Global Reactive Power')

fig.tight_layout()
fig.subplots_adjust(hspace=0.5, wspace=0.2)

plt.show()

# %%
import matplotlib.pyplot as plt

def plot(column, ax):
    ax.plot(data['DateTime'], data[column], color='black')
    ax.set_ylabel(column)
    ax.set_xlabel('Date')
    ax.set_title(f'{column} over time')

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

plot('Global_active_power', axs[0, 0])
plot('Sub_metering_1', axs[0, 1])
plot('Sub_metering_2', axs[0, 1])
plot('Sub_metering_3', axs[0, 1])
plot('Voltage', axs[1, 0])
plot('Global_reactive_power', axs[1, 1])

fig.subplots_adjust(hspace=0.5, wspace=0.2)

plt.show()

# %%
