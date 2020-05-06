### Declinacion Solar  ###4

#Blibliotecas requeridas

import matplotlib.pyplot as plt ## paquete matplotlib
import numpy as np   ## paquete numpy

from numpy import arange,cos,tan,pi  #importamos funciones

###----- Script--------##

n=np.arange(0,366)  

dec=-23.45*cos((360*pi*n)/(365*180))

plt.grid (True)
plt.title("Declinación Solar")
plt.xlabel ("Días del Año")
plt.ylabel ("Angulo de declinación °")
plt.plot(n,dec,"red")
plt.show()


