# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 01:33:05 2020

@author: HP
"""

### LINEAR CLASSIFIER ###
import numpy as np
import matplotlib.pyplot as plt

# Sample data X
X = np.array([[3,1], [2,5], [1,8], [6,4], [5,2], [3,5], [4,7], [4,-1]])

# y-list contains two categories (0's and 1's)
# X[a > b] == class_0, X[a < b] == class_1
y = [0, 1, 1, 0, 0, 1, 1, 0]

# Separating X-data into 0's and 1's
# Mapping the data to it's respective category
# By creating two lists
class_0 = np.array([X[i] for i in range(len(X)) if y[i] == 0])
class_1 = np.array([X[i] for i in range(len(X)) if y[i] == 1])

# Plotting a figure
plt.figure()

# Assigning markers for each category to the figure
plt.scatter(class_0[:, 0], class_0[:, 1], color='black', marker='s') # Category 0 represented with squares
plt.scatter(class_1[:, 0], class_1[:, 1], color='black', marker='x') # Category 1 represented with crosses

# Creating a seperating line
# with length and range to be 10
line_X = range(10)
line_y = line_X

plt.figure()
plt.scatter(class_0[:, 0], class_0[:, 1], color='black', marker='s')
plt.scatter(class_1[:, 0], class_1[:, 1], color='black', marker='x')
plt.plot(line_X, line_y, color='black', linewidth=3)
plt.show()