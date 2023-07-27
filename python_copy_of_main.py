import numpy as np
import pandas as pd
from scipy.fft import fft, ifft
import cmath
import matplotlib.pyplot as plt


data = pd.read_csv('with_object.s2p', sep=' ', header=None, skiprows=9, 
                names=['Frequency', 'ReS11', 'ImS11', 'ReS21', 'ImS21', 'ReS12', 'ImS12', 'ReS22', 'ImS22'])


data['s11']=data['ReS11']+1j*data['ImS11']
data['s21']=data['ReS21']+1j*data['ImS21']
data['s12']=data['ReS12']+1j*data['ImS12']
data['s22']=data['ReS22']+1j*data['ImS22']

data = data.drop(['ReS11', 'ImS11', 'ReS21', 'ImS21', 'ReS12', 'ImS12', 'ReS22', 'ImS22'], axis=1)


s_par = ['s11', 's21', 's12', 's22'] # Вести сюда названия S-параметров, которые нужны на графике в формате 'sij'


'''Дальше  не трогать'''
fig = plt.figure(figsize=(13,4))

ax_1 = fig.add_subplot(121)
for elem in s_par:
    ax_1.plot(data['Frequency']*1e-9, data[elem].apply(abs), label=elem)
ax_1.set_xlabel("Frequency, GHz")
ax_1.set_ylabel("Absolute value")
plt.legend()
plt.grid()

ax_2 = fig.add_subplot(122)
for elem in s_par:
    ax_2.plot(data['Frequency']*1e-9, np.degrees(data[elem].apply(cmath.phase)), label=elem)
ax_2.set_xlabel("Frequency, GHz")
ax_2.set_ylabel("Phase, deg")
plt.legend()
plt.grid()

fig.suptitle('Not processed data')
#plt.tight_layout()
plt.show()