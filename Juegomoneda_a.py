import random


exito = 0 
fracaso = 0

for j in range(10000):
    x = 2
    while  0 < x < 5:
        juego = random.choice(["jugador1","jugador2"])
        if juego == "jugador1":
            x += 1
            
        elif juego == "jugador2":
            x -= 1
            
        
    if x == 5:
        exito += 1
        
    elif x == 0:
        fracaso += 1
            
probabilidad = fracaso/100
print("La probabilidad de ruina es: ",probabilidad,"%" )
            

