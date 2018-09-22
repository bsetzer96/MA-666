# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:11:36 2018

@author: bever
"""

import numpy as np
import matplotlib.pyplot as plt


C=4      #capacitance
I=1      #current
dt=0.01  #time step
Vth=1    #threshold
Vreset=0 #reset voltage

t= np.linspace(0,10,1001) #time vector

v = np.zeros([1001,1]) #preallocating space
v[0] = 0.2              #initial condition

for n in np.arange(1000):
    v[n+1] = v[n] +dt*(I/C) 
    if v[n+1] > Vth:
        v[n+1]= Vreset
    
plt.plot(t,v)
plt.xlabel('time')
plt.ylabel('voltage')

