import random

def monte_carlo_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)  # Génère un x aléatoire entre -1 et 1
        y = random.uniform(-1, 1)  # Génère un y aléatoire entre -1 et 1

        # Vérifie si le point (x, y) est à l'intérieur du cercle
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # La valeur de π est approximée par le ratio des points dans le cercle au total des points, multiplié par 4
    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate

if __name__ == "__main__":
    num_points = 1000000  # Nombre de points à générer
    pi_value = monte_carlo_pi(num_points)
    print(f"Estimation de π avec {num_points} points : {pi_value}")
