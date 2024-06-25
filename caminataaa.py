import numpy as np

def random_walk(steps):
    # Inicializar posiciones
    x = [0]
    y = [0]

    # Definir posibles direcciones
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for _ in range(steps):
        # Escoger un índice de dirección aleatorio
        idx = np.random.choice(len(directions))
        dx, dy = directions[idx]

        # Moverse en la dirección escogida
        x.append(x[-1] + dx)
        y.append(y[-1] + dy)

    # Calcular la distancia desde el punto final al origen
    distance = abs(x[-1]) + abs(y[-1])
    return distance

def probability_within_threshold(num_walks, steps, threshold):
    count_within_threshold = 0

    for _ in range(num_walks):
        distance = random_walk(steps)
        if distance <= threshold:
            count_within_threshold += 1

    probability = count_within_threshold / num_walks
    return probability

num_walks = 500
threshold = 4
target_probability = 0.5

# Búsqueda iterativa para encontrar el número de pasos
min_steps = 1
max_steps = 45
tolerance = 0.05

while True:
    steps = (min_steps + max_steps) // 2
    probability = probability_within_threshold(num_walks, steps, threshold)

    if abs(probability - target_probability) < tolerance:
        break
    elif probability < target_probability:
        min_steps = steps
    else:
        max_steps = steps

print("Número de pasos necesarios para obtener una probabilidad del 50%:", steps)