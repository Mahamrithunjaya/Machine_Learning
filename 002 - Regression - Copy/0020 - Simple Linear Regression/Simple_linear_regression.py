# -*- coding: utf-8 -*-
"""Copy of simple_linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L3nZQRZjzN5DHLTP9jiSiY-ykzJYtkvc

# Simple Linear Regression

## Importing the libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""## Importing the dataset"""

dataset = pd.read_csv('Salary_Data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""## Training the Simple Linear Regression model on the Training set"""

from sklearn.linear_model import LinearRegression

# Creating an object of the LinearRegression class
regressor = LinearRegression()

# Training our regression model here using fit method of LinearRegression class
regressor.fit(X_train, y_train)

"""## Predicting the Test set results"""

y_pred = regressor.predict(X_test)

"""## Predicting the Train set results"""

X_train_pred = regressor.predict(X_train)

"""## Visualising the Training set results"""

plt.scatter(X_train, y_train, color = 'red')

plt.plot(X_train, X_train_pred, color = 'blue')

plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""## Visualising the Test set results"""

plt.scatter(X_test, y_test, color = 'red')

plt.plot(X_train, X_train_pred, color = 'blue')

plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""# **DOUBTS**

###FOR MORE CLARIFICATION
"""

plt.scatter(X_test, y_test, color = 'red')

plt.plot(X_test, y_pred, color = 'blue')

plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""*Since we have predicted the coefficients b0 and b1, they will be on the same line.*"""

plt.scatter(X_train, X_train_pred, color = 'red')

plt.scatter(X_test, y_pred, color = 'blue')

plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()