import random

def car_goat_simulation(num_experiments):
    success_switch = 0
    success_stay = 0

    for _ in range(num_experiments):
        # Randomly place the car behind one of the three doors
        car_position = random.randint(0, 2)

        # Contestant makes a choice
        choice = random.randint(0, 2)

        # Monty opens a door revealing a goat (not the contestant's choice or the car)
        available_doors = [door for door in range(3) if door != choice and door != car_position]
        door_opens = random.choice(available_doors)

        # If contestant switches, they choose the remaining unopened door
        switch_choice = [door for door in range(3) if door != choice and door != door_opens][0]

        # Check if switching would win the car
        if switch_choice == car_position:
            success_switch += 1

        # Check if staying would win the car
        if choice == car_position:
            success_stay += 1

    return success_switch, success_stay


# Number of experiments
num_experiments = 100

# Run the simulation
results = car_goat_simulation(num_experiments)

print(f"Number of successes if you switch: {results[0]}")
print(f"Number of successes if you do not switch: {results[1]}")

# Schlussfolgerung
# Anhand der Simulationsergebnisse können wir Folgendes feststellen:
#
# Wechseln von Türen: Die Erfolgsquote beim Türwechsel liegt bei etwa 2/3 (ca. 66,67 %). Das bedeutet, dass das Wechseln der Türen in etwa 2 von 3 Fällen zum Gewinn des Autos führt.
# Türen nicht wechseln: Die Erfolgsquote, wenn die Türen nicht gewechselt werden, liegt bei etwa 1/3 (ca. 33,33 %). Das bedeutet, dass in etwa 1 von 3 Fällen das Festhalten an der ursprünglichen Wahl zum Gewinn des Autos führt.
#
# Die Simulation bestätigt die widersprüchliche Schlussfolgerung des Monty-Hall-Problems: Es ist statistisch gesehen immer vorteilhaft, die Türen zu wechseln. Dieses Ergebnis kommt zustande, weil die ursprüngliche Wahl mit einer Wahrscheinlichkeit von 1/3 richtig ist und der Wechsel die höhere Wahrscheinlichkeit von 2/3, dass sich das Auto hinter einer der beiden anderen Türen befindet, ausnutzt.
# Aus meiner Sicht bedeutet das jedoch realistisch gesehen, dass es keinen tatsächlichen Unterschied macht, ob man die Tür wechselt oder nicht und ist ein rein statistischer und theoretischer Wert.
