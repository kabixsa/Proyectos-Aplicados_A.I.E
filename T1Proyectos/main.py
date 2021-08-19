import numpy as np
import matplotlib.pyplot as plt

def seno(z):
    return np.sin(z)

a=0
b=2*np.pi
espaciamiento=30

x=np.linspace(a,b,int(360/espaciamiento+1))

f=seno(x)


plt.plot(x,f)
plt.plot(x,f,'o')
plt.grid(True)
plt.show()