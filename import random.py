import random

def loteria_paso_a_paso():
    numeros_disponibles = list(range(1, 21))
    random.shuffle(numeros_disponibles)  # Mezcla aleatoriamente los números

    print("¡Comienza la lotería!")
    print("Presiona ENTER para revelar cada número...\n")

    for i, numero in enumerate(numeros_disponibles, start=1):
        input(f"Número {i}: ")
        print(f"→ {numero}\n")

    print("¡Se han revelado los 20 números!")

if __name__ == "__main__":
    loteria_paso_a_paso() 