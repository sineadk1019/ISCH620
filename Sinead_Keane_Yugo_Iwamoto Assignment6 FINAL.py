# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:02:32 2023
Name: Sinead Keane & Yugo Iwamoto
Class: ISCH 620
Due Date: 12/10/2023
Assignment #6, Group Project 
Email: sinead.keane001@gmail.com
Email:  yi9686@rit.edu
"""
#pip install numpy 
#pip install matplolib

import matplotlib.pyplot as plt
import numpy as np


# Data created from a random.seed and then put into an Numpy ndarray:
    #loc - float or array_like of floats (mean of distribution)
    #scale - std. deviation (spread or width) of distribution MUST BE NON-NEG
    #size - Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn. 
    #If size is None (default), a single value is returned if loc and scale are both scalars. 
    #Otherwise, np.broadcast(loc, scale).size samples are drawn.
    #(Above information provided by Matplotlib.com)
np.random.seed (10)
fig1 = np.random.normal(1.2,1, size= (10,10))

#Checking the randomized array. This made a two dimensional Numpy array (ndarray)
#print(fig1)
#print(type(fig1))

# Plot the N ndarray based on Matplotlib tutorial (can provide if requested)
fig, ax = plt.subplots()

vp = ax.violinplot(fig1, showmeans=True, showextrema=True, showmedians=True)

#Sets the axises on the graph.
ax.set(xlim=(-1, 12), xticks=np.arange(2, 12, 2),
       ylim=(-2, 4), yticks=np.arange(-1, 4, 1))

#Shows the above plot visually.
plt.show()