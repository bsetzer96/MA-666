# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:10:48 2018

@author: bever
"""

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

data=sio.loadmat('EEG-2.mat')

EEG=data['EEG']
t=data['t']

ntrials = EEG.shape[0]            # ... and compute the number of trials.

mn = np.mean(EEG,0)               # Compute the mean signal across trials (the ERP)
sd = np.std(EEG,0)                # Compute the std of the signal across trials
sdmn = sd / np.sqrt(ntrials)       # Compute the std of the mean

plt.figure(figsize=(12,3))                   # Resize the figure
plt.plot(t[0,:], mn, 'k', lw=3)              # Plot the ERP of condition A
plt.plot(t[0,:], mn + 2 * sdmn, 'k:', lw=1)  # ... and include the upper CI
plt.plot(t[0,:], mn - 2 * sdmn, 'k:', lw=1)  # ... and the lower CI
plt.xlabel('Time [s]')                       # Label the axes
plt.ylabel('Voltage [$\mu$ V]')
plt.title('ERP of condition A')              # ... provide a useful title
plt.show()      


import scipy.io as sio
data = sio.loadmat('EEG-1.mat')

data.keys()

EEGa = data['EEGa']
EEGb = data['EEGb']
t = data['t']


plt.plot(EEGa[0, :])               # Plot the data from condition A, trial 1.
plt.show()


plt.plot(t[0,:], EEGa[0, :])                     # Plot condition A, trial 1 data vs t.
plt.xlabel('Time [s]')                           # Label the x-axis as time.
plt.ylabel('Voltage [$\mu$ V]')                  # Label the y-axis as voltage.
plt.title('EEG data from condition A, Trial 1')  # Add a title

# Add a vertical line to indicate the stimulus time
plt.plot([0.25, 0.25], [-4,4], 'k', lw=2)

plt.show()