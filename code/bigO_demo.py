# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 08:31:30 2020

@author: https://www.linkedin.com/in/gabrieltribeiro/
"""
import matplotlib.pyplot as plt
import numpy as np
import timeit

def const_O(x):
    x[0]**2
    
def linear_O(x):
    for item in range(len(x)):
        x[item]**2
        
def quadratic_O(x):
    for item_1 in range(len(x)):
        for item_2 in range(len(x)):
            x[item_1]*x[item_2]

times_const = []
times_linear = []
times_quad = []

dims = np.linspace(1, 10, 10)
for x_size in dims:
    
    start_time = timeit.default_timer()
    const_O(np.ones(int(x_size)))
    times_const.append(timeit.default_timer() - start_time)
    
    start_time = timeit.default_timer()
    linear_O(np.ones(int(x_size)))
    times_linear.append(timeit.default_timer() - start_time)
    
    start_time = timeit.default_timer()
    quadratic_O(np.ones(int(x_size)))
    times_quad.append(timeit.default_timer() - start_time)

plt.figure(figsize=(10,5))
plt.plot(dims, times_const)
plt.plot(dims, times_linear)
plt.plot(dims, times_quad)
plt.legend(['O(c)', 'O(x)', 'O(x**2)'])
plt.xlabel('Input dimension', fontsize='large')
plt.ylabel('Execution time', fontsize='large')
plt.xticks(ticks=dims)
plt.grid()
    
    

