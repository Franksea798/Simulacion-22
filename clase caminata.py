import random

def caminata(n):
    x = 0
    for i in range(n):
        paso = random.choice(["E", "O"])
        if paso == "E":
            x = x + 1
        else:
            x = x - 1
    return x

# Primer bucle
for i in range(25):
    c = caminata(10)
    print(c, "distancia =", abs(c))

# Segundo bucle
numero_caminatas = 50000
for longitud in range(40, 80):
    exitos = 0
    for i in range(numero_caminatas):
        x = caminata(longitud)
        distancia = abs(x)
        if distancia <= 4:
            exitos += 1
    porcentaje = float(exitos / numero_caminatas)
    print("pasos =", longitud, "/%exitos", 100 * porcentaje)