from random import random
from math import sin,pi

f = lambda x : (8/pi**2)*x

g = lambda x : sin(x)

def estimador(n,a,b):
    s = 0
    u = (b-a)*random()+a
    for i in range(n):
        s+=g(u)/f(u)
    return s/n


print(estimador(1000000,0,pi/2))