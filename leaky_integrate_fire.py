# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

#define variables
I=1
R=1
tau=5
t=np.linspace(0,10,101)
y=np.zeros(101)
y0=0
y[0]=y0
h=0.1

def lif(I,R,tau,v):
    dv=-(1/tau)*v+(R/tau)*I
    return dv

for n in np.arange(100):
    y[n+1]=y[n] +h*lif(I,R,tau,y[n])
    
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('voltage')



