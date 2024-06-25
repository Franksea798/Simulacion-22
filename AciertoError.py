import random
import math

acierto = 0

for i in range (0,10000):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    
    f = (math.exp(x) - 1)/(math.e - 1)
    
    if f > y:
        acierto += 1 
    
    else: 
        acierto = acierto

integral = acierto / 10000

print("El valor de la integral en el intervalo (0,1) =", integral )