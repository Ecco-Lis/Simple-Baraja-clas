import random

class Baraja:
    def __init__(self):
        """
        Inicializa una nueva baraja de cartas española.
        """
        palos = ['o', 'c', 'e', 'b']  # Definición de los cuatro palos: Oros, Copas, Espadas, Bastos
        numeros = ['A', '1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']  # Números y figuras
        self.cartas = [num + palo for palo in palos for num in numeros]

    def barajar(self):
        """
        Baraja las cartas en la baraja de forma aleatoria.
        
        Utiliza el algoritmo de mezcla Fisher-Yates.
        """
        n = len(self.cartas)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

    def repartir(self, mano, jugadores):
        """
        Reparte cartas a los jugadores.

        :param mano: Número de cartas a repartir a cada jugador.
        :param jugadores: Número total de jugadores.
        :return: Lista de listas que representan las manos de los jugadores.
        """
        if mano * jugadores <= len(self.cartas):
            manos = []
            for _ in range(jugadores):
                mano_actual = [self.cartas.pop() for _ in range(mano)]
                manos.append(mano_actual)
            return manos
        else:
            return "No hay suficientes cartas en la baraja para repartir."

def main():
    mi_baraja = Baraja()
    # Uso de colores ANSI para el mensaje de bienvenida
    print("\033[1;32m¡Bienvenido al juego de la baraja!\033[0m")

    while True:
        print("\nOpciones:")
        print("1. Mostrar las cartas en la baraja")
        print("2. Mezclar las cartas")
        print("3. Repartir cartas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Cartas en la baraja:", mi_baraja.cartas)
        elif opcion == "2":
            mi_baraja.barajar()
            # Uso de colores ANSI para el mensaje de cartas mezcladas
            print("\033[1;33mCartas mezcladas.\033[0m")
        elif opcion == "3":
            mano = int(input("Ingresa el número de cartas por jugador: "))
            jugadores = int(input("Ingresa el número total de jugadores: "))
            manos = mi_baraja.repartir(mano, jugadores)
            print("\nCartas repartidas:")
            for i, mano in enumerate(manos, start=1):
                # Uso de colores ANSI para los nombres de los jugadores
                print(f"Jugador \033[1;34m{i}\033[0m: {mano}")
        elif opcion == "4":
            # Uso de colores ANSI para el mensaje de despedida
            print("\033[1;31m¡Hasta luego!\033[0m")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()


