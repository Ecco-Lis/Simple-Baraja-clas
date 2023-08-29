import random

class Baraja:
    def __init__(self):
        palos = ['o', 'c', 'e', 'b']
        numeros = ['A', '1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
        self.cartas = [num + palo for palo in palos for num in numeros]

    def barajar(self):
        n = len(self.cartas)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

    def repartir(self, mano, jugadores):
        if mano * jugadores <= len(self.cartas):
            manos = []
            for _ in range(jugadores):
                mano_actual = [self.cartas.pop() for _ in range(mano)]
                manos.append(mano_actual)
            return manos
        else:
            return "No hay suficientes cartas en la baraja."

def main():
    mi_baraja = Baraja()
    print("\033[1;32mBienvenido al juego de la baraja!\033[0m")

    while True:
        print("\nOpciones:")
        print("1. Mostrar cartas en la baraja")
        print("2. Barajar la baraja")
        print("3. Repartir cartas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Cartas en la baraja:", mi_baraja.cartas)
        elif opcion == "2":
            mi_baraja.barajar()
            print("\033[1;33mBaraja barajada.\033[0m")
        elif opcion == "3":
            mano = int(input("Ingrese el número de cartas por mano: "))
            jugadores = int(input("Ingrese el número de jugadores: "))
            manos = mi_baraja.repartir(mano, jugadores)
            print("\nManos repartidas:")
            for i, mano in enumerate(manos, start=1):
                print(f"Jugador \033[1;34m{i}\033[0m: {mano}")
        elif opcion == "4":
            print("\033[1;31m¡Hasta luego!\033[0m")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
