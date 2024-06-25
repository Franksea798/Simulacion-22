from random import expovariate
from matplotlib.pyplot import *
from random import seed
from math import inf as Infinity
from statistics import mean

tpll = 2.0
tps = 1.0
T = 100.0
t = 0.0

N = 0

T_arrivo = expovariate(1/tpll)

T_salida = Infinity

X = []
Y = []

while t <= T:
    tll = expovariate(1/tpll)
    ts = expovariate (1/tps)
    
    if tll <= ts:
        N += 1
        t = t + tll
        X.append(t)
        Y.append(N)
    
    else:
        if N > 0:
            N -= 1
            t = t + ts
            X.append(t)
            Y.append(N)
    
fig = figure(1, figsize = (16, 8))
step(X, Y, linewidth = 1.2, color = "black")
xlabel("Tiempo", size = 16)
ylabel("N", size = 16)
show()