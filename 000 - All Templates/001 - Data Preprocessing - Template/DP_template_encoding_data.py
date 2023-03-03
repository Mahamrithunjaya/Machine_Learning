# -*- coding: utf-8 -*-
"""Copy of data_preprocessing_template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19KJp6ULu7Bz7r9w3fzqFo8LAlzHFj373

# Data Preprocessing Template

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""# Encoding categorical data

## Encoding the Variable
"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),
                                      ['column-index want to encode'])],
                        remainder='passthrough')
X = np.array(ct.fit_transform(X))

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state = 0)