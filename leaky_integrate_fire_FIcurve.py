# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

#define variables
I=10
R=1
C=1
tau=R*C
t=np.linspace(0,10,101)
y=np.zeros(101)
h=0.1
v_th=-48
v_rest=-60
vstar=v_rest+I*R
y0=v_rest
v_reset=v_rest-5
y[0]=y0

def lif(vstar,tau,v):
    dv=-(v-vstar)/tau
    return dv
    
for n in np.arange(100):
    y[n+1]=y[n] +h*lif(vstar,tau,y[n])
    if y[n+1]>v_th:
        y[n+1]=v_reset
   

    
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('voltage')
    


