import random 
import math 
from statistics import mean, median
from matplotlib.pyplot import *
l= [946,1058,1133,869,927,742,1113,665,955,1288,1074,838,815,910,1193,
    1386,955,1187,891,1302,867,837,1138,868,969,737,1143,947,763,1029]
# Esta funcion implementa una prueba de corridas
def prueba_corridas(l):
    
    l_median = mean(l)  # Hacemos la prueba respecto a la media/mediana
    
    R, n1, n2 = 1, 0, 0   # iniciamos los contadores
        
    for i in range(len(l)):    
        
        # Aumentamos R cuando 2 entradas están una arriba y otra abajo de la media/mediana:
        if (l[i] >= l_median and l[i-1] < l_median) or (l[i] < l_median and l[i-1] >= l_median):
            R += 1
        # Contamos las que están arriba y las que están abajo
        if(l[i]) >= l_median:
            n1 += 1
        else:
            n2 += 1   
    # calculamos los parámetros y el estadistico
    R_exp = ((2*n1*n2)/(n1+n2))+1
    stan_dev = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/(((n1+n2)**2)*(n1+n2-1))) 
  
    z = (R - R_exp)/stan_dev 
  
    return R, n1, n2, R_exp, z, stan_dev 
R = prueba_corridas(l)[0]
n1 = prueba_corridas(l)[1]
n2 = prueba_corridas(l)[2]
R_exp = abs(prueba_corridas(l)[3])
Z = abs(prueba_corridas(l)[4]) 
stan_dev = abs(prueba_corridas(l)[5])

print('Estadistico = ', Z)
print('  R = ', R, '  R_exp = ', R_exp, '\n n1 = ', n1, '\n n2 = ', n2, '\nVarianza = ', stan_dev**2)