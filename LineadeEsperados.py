from random import expovariate
from matplotlib.pyplot import *
from random import seed
from math import inf as Infinity
from statistics import mean

tpll = 2.0        # Tiempo promedio
T = 15            # Tiempo total del sistema

N = 0             # Variable de estadistica

t = 0             # Horas de simulación

llegadas = []
num = []

while t <= T:
    N = N + 1
    # Avance del tiempo simulado 
    t = t + expovariate(1/tpll)
    llegadas.append(t)
    num.append(N)

step(llegadas, num)
print("Numero total de llegadas= ", N)