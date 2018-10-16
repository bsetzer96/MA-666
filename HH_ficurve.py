# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:49:11 2018

@author: bever
"""
#NOTE: this will not work for the default HH function!
#edited the HH file to return dv and take in dt

import numpy as np
import matplotlib.pyplot as plt
from HH_functions import HH

T0= 500 #number of time points
n=200 # length of I vector
I= np.linspace(0,100,n)   #input
dt = 0.01;
T  = T0/dt  # [ms]
FI_rate = np.zeros(n)

for j in np.arange(n):
    I0=I[j]
    V,m,h,n,t,dv = HH(I0, T0, dt)
    
    num_peaks = 0
    for i in np.arange(T-1):
        if dv[int(i)]>0 and dv[int(i+1)]<0:
            num_peaks = num_peaks+1
    FI_rate[j] = num_peaks

plt.plot(I, FI_rate)
plt.xlabel("Imput current(I)")
plt.ylabel("Number of Spikes")
plt.show()