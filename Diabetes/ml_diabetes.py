# -*- coding: utf-8 -*-
"""ML_Diabetes

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nPjMUI9_E51TRB4v5M2o-NssN7nOOPIO
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

# Read the data
calories = pd.read_csv('calories.csv')

# Print the first 5 rows of the data
print(calories.head())

#Read the exercise.csv file
exercise = pd.read_csv('exercise.csv')

# Print the first 5 rows of the data
print(exercise.head())

#combine the two datasets
calories_data = pd.concat([exercise, calories['Calories']], axis=1) 
print(calories_data.head())

#checking the number of rows and columns
print(calories_data.shape)

#getting more info about the dataset
print(calories_data.info())

#checking for missing values
print(calories_data.isnull().sum())

calories_data.info

# stastical Data about the dataset
calories_data.describe()

"""Data Visualization

"""

#Plotting the Gender plot
sns.countplot(calories_data['Gender'])

#Finding the dsitribution of Age
sns.distplot(calories_data['Age'])

#Finding the dsitribution of height
sns.distplot(calories_data['Height'])

sns.distplot(calories_data['Weight'])

sns.distplot(calories_data['Heart_Rate'])

"""Co-Relation in dataset"""

corrr = calories_data.corr()

"""1. Positive Correlation
2. negetive Correlation
"""

#contructing a heatmap to understand the relation
plt.figure(figsize=(10,10))
sns.heatmap(corrr, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':18}, cmap='Blues')

#Converting the text data to numerical Values
calories_data.replace({'Gender':{'male':0,'female':1}}, inplace=True)

calories_data.head()

#Seperating Features and Targets
X=calories_data.drop(columns=['User_ID','Calories'], axis=1)
Y=calories_data['Calories']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""MODEL Trainning
XGBoost Regressor
"""

#loading the model
model = XGBRegressor()

#Trainning the data
model.fit(X_train, Y_train)

"""Evaluating the Model

Prediction on test data
"""

test_data_prediction = model.predict(X_test)

print(test_data_prediction)

"""Comparing the test with the already saved values

Mean Absolute Error
"""

mae = metrics.mean_absolute_error(Y_test, test_data_prediction)

print("Mean Absolute Error:", mae)