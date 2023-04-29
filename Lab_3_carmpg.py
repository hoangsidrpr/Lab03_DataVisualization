# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 21:53:34 2015

@author: nymph
"""

# %%
#################################### Read the data ############################
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

''' read_csv()
The read_csv() function in pandas package parse an csv data as a DataFrame data structure. What's the endpoint of the data?
The data structure is able to deal with complex table data whose attributes are of all data types. 
Row names, column names in the dataframe can be used to index data.
'''

data = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original", delim_whitespace=True,
                   header=None, names=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model', 'origin', 'car_name'])

data['mpg']
data.mpg
data.iloc[0, :]

print(data.shape)

################################## Enter your code below ######################

################################## Q6 ######################
def q6_plot():
    plt.scatter(data.model, data.cylinders + np.random.random(len(data['cylinders'])))
    plt.xlabel('Model')
    plt.ylabel('Cylinders')
    plt.title('Scatter of Model and Cylinders')
    plt.savefig('q6.png', bbox_inches='tight')
    plt.show()
q6_plot()

################################## Q7 ######################
def q7_plot1():
    plt.scatter(data.displacement, data.mpg);
    plt.ylabel('MPG')
    plt.xlabel('Displacement')
    plt.title('Scatter of MPG and Displacement')
    plt.savefig('q7_1.png', bbox_inches='tight')
    plt.show()
q7_plot1()

def q7_plot2():
    plt.scatter(data.horsepower, data.mpg);
    plt.ylabel('MPG')
    plt.xlabel('Horsepower')
    plt.title('Scatter of MPG and Horsepower')
    plt.savefig('q7_2.png', bbox_inches='tight')
    plt.show()
q7_plot2()

################################## Q8 #########################################
data_ = data.copy()
data_['type_car'] = data_.car_name.str.split().str.get(0)
q8 = data_.groupby(['model'])
q8_data = q8['type_car'].count()


def q8_plot():
    ''' Create a canvas with width 10, height 7.5 '''
    fig_obj = plt.figure(figsize=(10, 7.5))
    sns.set_style("whitegrid")
    sns.lineplot(data=q8_data, legend='auto', color='orange', marker='o').set(
        title='A number of new cars introduced each year', xlabel='model', ylabel='count')

    ax = plt.subplot(111)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ''' Save figure '''
    plt.tight_layout()
    plt.savefig('q8.png', bbox_inches='tight')
    plt.show()


q8_plot()

################################## Q9 #########################################
q9_data = data.iloc[:, :8].corr()


def q9_plot():
    ''' Create a canvas with width 10, height 7.5 '''
    fig_obj = plt.figure(figsize=(10, 7.5))
    sns.heatmap(q9_data, annot=True)

    ''' Save figure '''
    # plt.tight_layout()
    plt.savefig('q9.png', bbox_inches='tight')
    plt.show()


q9_plot()

# %%
# Q4

def q4_plot():
    data.hist(bins=12, figsize=(15, 6), layout=(2, 4))
    plt.tight_layout()
    plt.savefig('q4.png', bbox_inches='tight')
    plt.show()


q4_plot()

# %% <- them cai nay vao de chay interactive python giong nhu ipynb cho de code (vscode)
# https://code.visualstudio.com/docs/python/jupyter-support-py
