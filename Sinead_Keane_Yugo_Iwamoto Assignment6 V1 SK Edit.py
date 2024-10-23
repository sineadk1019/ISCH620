# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:02:32 2023
Name: Sinead Keane & Yugo Iwamoto
Class: ISCH 620
Due Date: 12/10/2023
Assignment #6, Group Project, V1 
Email: sinead.keane001@gmail.com
Email:  yi9686@rit.edu
"""
#pip install numpy 
#pip install matplolib

import matplotlib.pyplot as plt
import numpy as np
import random

# make data:
#loc - float or array_like of floats (mean of distribution)
#scale - std. deviation (spread or width) of distribution MUST BE NON-NEG
#size - Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn. 
# If size is None (default), a single value is returned if loc and scale are both scalars. 
#Otherwise, np.broadcast(loc, scale).size samples are drawn.
np.random.seed (20)
fig1 = np.random.normal(5.5, 2.9, size= (10,2))

#checking the array
print(fig1)
print(type(fig1))

# plot - some code from https://matplotlib.org/stable/plot_types/stats/violin.html
fig, ax = plt.subplots()

vp = ax.violinplot(fig1,showmeans=False, showmedians=False, showextrema=False)

# styling from matplotlib; not quite sure what this is. 
for body in vp['bodies']:
    body.set_alpha(0.9)

#sets the axises
ax.set(xlim=(-1, 11), xticks=np.arange(2, 12, 2),
       ylim=(-2, 4), yticks=np.arange(-1, 4, 1))

plt.show()