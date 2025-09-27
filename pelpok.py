import random

nombre_entrenador1 = input("Nombre del entrenador 1: ")
nombre_pokemon1 = input("Nombre del pokemon 1: ")
ataque1 = random.randint(20, 100)
vida_max1 = random.randint(150, 400)
vida1 = vida_max1

ganadas, perdidas = 0, 0

while True:
    opcion = input("\nPelear (P) o Finalizar (F): ").upper()
    if opcion == "F":
        print("\nEntrenador:", nombre_entrenador1)
        print("Pokemon:", nombre_pokemon1)
        print("Ataque máximo:", ataque1)
        print("Vida máxima:", vida_max1)
        print("Ganadas:", ganadas)
        print("Perdidas:", perdidas)
        break

    nombre_entrenador2 = input("Nombre del entrenador 2: ")
    nombre_pokemon2 = input("Nombre del pokemon 2: ")
    ataque2 = random.randint(20, 100)
    vida_max2 = random.randint(150, 400)
    vida2 = vida_max2

    vida1 = vida_max1
    vida2 = vida_max2
    turno = 1

    while vida1 > 0 and vida2 > 0:
        if turno == 1:
            golpe = random.randint(0, ataque1)
            if random.randint(1, 6) == 6: golpe = 0
            vida2 -= golpe
            print(f"{nombre_pokemon1} atacó con {golpe}. Vida de {nombre_pokemon2}: {vida2}")
            turno = 2
        else:
            golpe = random.randint(0, ataque2)
            if random.randint(1, 6) == 6: golpe = 0
            vida1 -= golpe
            print(f"{nombre_pokemon2} atacó con {golpe}. Vida de {nombre_pokemon1}: {vida1}")
            turno = 1

    if vida1 > 0:
        print(f"\nGanó {nombre_entrenador1} con {nombre_pokemon1}")
        ganadas += 1
    else:
        print(f"\nGanó {nombre_entrenador2} con {nombre_pokemon2}")
        perdidas += 1
