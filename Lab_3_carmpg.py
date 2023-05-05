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
# %%
# Q1 ---

# %%
# Q2 ---

# %%
# Q3 ---
print(data.isna().sum())
print(data.describe())

data['mpg'].fillna(int(data['mpg'].mean()), inplace=True)
data['horsepower'].fillna(int(data['horsepower'].mean()), inplace=True)
print(data.isna().sum())
# %%
# Q4 


def q4_plot():
    data.hist(bins=13, figsize=(15, 6), layout=(2, 4),
              linewidth=1.2, edgecolor='white')
    plt.tight_layout()
    plt.savefig('q4.png', bbox_inches='tight', dpi=500)
    plt.show()


q4_plot()

# %%
# Q5
def q5_plot():
    fig_obj = plt.figure(figsize=(10, 7.5))
    ax = plt.subplot(111)

    p = plt.plot(data.mpg, data.weight, 'r.')
    plt.ylabel('Weight')
    plt.xlabel('MPG')
    plt.title('Scatter of MPG and Weight')
    plt.savefig('q5.png',bbox_inches='tight',dpi=300)
    plt.show()

q5_plot()

def correlation(x, y):
    mean_x = sum(x)/float(len(x))
    mean_y = sum(y)/float(len(y))
    
    sub_x = [i-mean_x for i in x]
    sub_y = [i-mean_y for i in y]
    
    numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
    
    std_deviation_x = sum([sub_x[i]**2.0 for i in range(len(sub_x))])
    std_deviation_y = sum([sub_y[i]**2.0 for i in range(len(sub_y))])
    # squaring by 0.5 to find the square root
    denominator = (std_deviation_x*std_deviation_y)**0.5
    
    cor = numerator/denominator
    return cor

print("He so tuong quan cua MPG va Weight: {}".format(correlation(data.mpg, data.weight)))
# %%
################################## Q6 ######################


def q6_plot():
    plt.scatter(data.model, data.cylinders +
                np.random.random(len(data['cylinders'])))
    plt.xlabel('Model')
    plt.ylabel('Cylinders')
    plt.title('Scatter of Model and Cylinders')
    plt.savefig('q6.png', bbox_inches='tight', dpi=300)
    plt.show()


q6_plot()

# %%
################################## Q7 ######################


def q7_plot1():
    plt.scatter(data.displacement, data.mpg)
    plt.ylabel('MPG')
    plt.xlabel('Displacement')
    plt.title('Scatter of MPG and Displacement')
    plt.savefig('q7_1.png', bbox_inches='tight', dpi=300)
    plt.show()


q7_plot1()


def q7_plot2():
    plt.scatter(data.horsepower, data.mpg)
    plt.ylabel('MPG')
    plt.xlabel('Horsepower')
    plt.title('Scatter of MPG and Horsepower')
    plt.savefig('q7_2.png', bbox_inches='tight', dpi=300)
    plt.show()


q7_plot2()

# %%
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
    plt.savefig('q8.png', bbox_inches='tight', dpi=500)
    plt.show()


q8_plot()

# %%
################################## Q9 #########################################
q9_data = data.iloc[:, :8].corr()


def q9_plot():
    ''' Create a canvas with width 10, height 7.5 '''
    fig_obj = plt.figure(figsize=(10, 7.5))
    sns.heatmap(q9_data, annot=True)

    ''' Save figure '''
    # plt.tight_layout()
    plt.xticks(rotation=45)
    plt.savefig('q9.png', bbox_inches='tight', dpi=500)
    plt.show()


q9_plot()

# %% <- them cai nay vao de chay interactive python giong nhu ipynb cho de code (vscode)
# https://code.visualstudio.com/docs/python/jupyter-support-py