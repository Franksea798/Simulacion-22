import random

zonas = ["negro","rojo","azul","verde"]
zonanegra = 0
zonarojo = 0
zonaazul = 0
zonaverde = 0
paso = 0

for i in range(0,10000):
    monedas = random.choice(["AA","AS","SA","SS"])

    if monedas == "AA":
        paso += 2

    elif monedas == "AS":
        paso += 1

    elif monedas == "SA":
        paso += 1

    else:
        paso += 0
    
    if paso > 3:
        paso =  paso - 4
    
    else:
        paso = paso
        
    zona = zonas[paso]
    
    if zona == "negro":
        zonanegra += 1
    
    elif zona == "rojo":
        zonarojo += 1
    
    elif zona == "azul":
        zonaazul += 1
    
    else:
        zonaverde += 1
        
print("La probabilidad de la zona negra es : ", zonanegra/100,"%")    
print("La probabilidad de la zona roja es : ", zonarojo/100,"%")    
print("La probabilidad de la zona azul es : ", zonaazul/100,"%")    
print("La probabilidad de la zona verde es : ", zonaverde/100,"%")    


