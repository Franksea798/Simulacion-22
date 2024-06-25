from random import expovariate
from matplotlib.pyplot import *
from random import seed

tpll = 2.0    #Tiempo promedio
T = 15        #Tiempo total
N = 0         #Variable de estadistica
t = 0         #Hora de simulación

while t <= T:
    N = N + 1
    #Avance del tiempo
    t = t + expovariate(1/tpll)

print ("numero de llegadas = ", N)
