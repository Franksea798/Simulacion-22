import random

pacientes = ["uno","dos","tres","cuatro","cero"]
cuno = 0
cdos = 0
ctres = 0
ccuatro = 0
ccero = 0
repeticiones = []
actual = random.choice(pacientes)
for i in range(0,10000):
    if actual == "cero":
        ccero += 1
        x = random.uniform(0,1)
        if x < 0.3:
            actual = "cero"
        elif x < 0.8:
            actual = "uno"
        else:
            actual = "dos"
    if actual == "uno":
        cuno += 1
        x = random.uniform(0,1)
        if x < 0.4:
            actual = "cero"
        elif x < 0.75:
            actual = "uno"
        elif x <0.8:
            actual = "tres"
        else:
            actual = "cuatro"
    if actual == "dos":
        cdos += 1
        x = random.uniform(0,1)
        if x < 0.2:
            actual = "cero"
        elif x < 0.4:
            actual = "uno"
        elif x < 0.6:
            actual = "dos"
        elif x < 0.8:
            actual = "tres"
        else:
            actual = "cuatro"
    if actual == "tres":
        ctres += 1
        x = random.uniform(0,1)
        if x < 0.33:
            actual = "cero"
        else:
            actual = "dos"
    if actual == "cuatro":
        ccuatro += 1
        x = random.uniform(0,1)
        if x < 0.5:
            actual = "cero"
        else:
            actual = "cuatro"
total = ccero + cuno + cdos + ctres + ccuatro

probabilidadcero = ccero/total
probabilidaduno = cuno/total
probabilidaddos = cdos/total
probabilidadtres = ctres/total
probabilidadcuatro = ccuatro/total
print("La probabilidad de tener 0 pacientes es: ", probabilidadcero)
print("La probabilidad de tener 1 pacientes es: ", probabilidaduno)
print("La probabilidad de tener 2 pacientes es: ", probabilidaddos)
print("La probabilidad de tener 3 pacientes es: ", probabilidadtres)
print("La probabilidad de tener 4 pacientes es: ", probabilidadcuatro)