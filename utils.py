import numpy as np
import random
from variables import eslora_barcos, simbolo_agua , simbolo_barco, simbolo_fallo, simbolo_impacto

class Barco:
    def __init__(self, eslora): # Define el constructor de la clase Barco
        self.eslora = eslora  # Asigna el valor de eslora (tamaño del barco) a la instancia
        self.coordenadas = [] # Inicializa una lista vacía para almacenar las coordenadas del barco
        self.orientacion = random.choice(['horizontal', 'vertical']) # Elige aleatoriamente la orientación del barco
        self.crear_barco() # Llama al método crear_barco para generar las coordenadas del barco

    def crear_barco(self): # Define el método crear_barco
        if self.orientacion == 'horizontal': # Si la orientación es horizontal:
            x = random.randint(0, 9 - self.eslora)  # Genera una coordenada "x" aleatoria para el inicio del barco
            y = random.randint(0, 9)  # Genera una coordenada "y" aleatoria para el inicio del barco
            self.coordenadas = [(x + i, y) for i in range(self.eslora)] # Crea una lista de coordenadas para el barco horizontal
        else: # Si la orientación es horizontal:
            x = random.randint(0, 9)  # Genera una coordenada "x" aleatoria para el inicio del barco
            y = random.randint(0, 9 - self.eslora) # Genera una coordenada "y" aleatoria para el inicio del barco
            self.coordenadas = [(x, y + i) for i in range(self.eslora)] # Crea una lista de coordenadas para el barco vertical

    def colocar_en_tablero(self, tablero): # Define el método colocar_en_tablero
        for x, y in self.coordenadas: # Itera sobre las coordenadas del barco
            tablero[x, y] = simbolo_barco # Marca las coordenadas del barco en el tablero con "O"(en variables)

    def esta_hundido(self, tablero): # Define el método esta_hundido
        return all(tablero[x, y] == simbolo_impacto for x, y in self.coordenadas) # Verifica si todas las coordenadas del barco están marcadas con "X" (en variables)

def crear_tablero(tamaño=10): # Define la función crear_tablero con un tamaño predeterminado de 10 />                                                  si meto en las variables el tamaño = 10 luego da fallo                      
    return np.full((tamaño, tamaño), simbolo_agua) # Crea y devuelve un tablero de tamaño 10 lleno de "_" (en variables)

def colocar_barcos(tablero): # Define la función colocar_barcos
    # barcos = [2, 2, 2, 3, 3, 4]Define una lista de esloras de barcos//ahora se definen en variables
    for eslora in eslora_barcos: # Itera sobre la lista de esloras
        while True: # Inicia un bucle infinito
            barco = Barco(eslora) # Crea una instancia de Barco con la eslora actual
            if all(tablero[x, y] == simbolo_agua for x, y in barco.coordenadas): # Verifica si todas las coordenadas del barco están libres
                barco.colocar_en_tablero(tablero) # Coloca el barco en el tablero
                break  # Rompe el bucle infinito si el barco se coloca correctamente

def disparo(tablero): # Define la función disparo
    fila = int(input("Selecciona la fila: ")) # Solicita al usuario que ingrese la fila para disparar
    columna = int(input("Selecciona la columna: ")) # Solicita al usuario que ingrese la columna para disparar
    if tablero[fila, columna] == simbolo_barco: # Si la posición en el tablero tiene un barco ("O")
        tablero[fila, columna] = simbolo_impacto  # Marca la posición como impactada ("X")
        print("_"*70)
        print()
        print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
        print("¡¡¡IMPACTOOOOO!!!")
        print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
        print("_"*70)
        return disparo(tablero)
    elif tablero[fila, columna] in [simbolo_fallo, simbolo_impacto]: # Si la posición ya ha sido seleccionada antes
        print("Posición ya seleccionada") # Informa al usuario que la posición ya ha sido seleccionada
        return disparo(tablero)  # Llamada recursiva para volver a intentar
    else: # Si la posición no tiene un barco
        tablero[fila, columna] = simbolo_fallo # Marca la posición como fallo/agua ("#")
        print("_"*70)
        print()
        print("🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊")
        print("FALLASTE :)")
        print("🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊")
        print("_"*70)
    return tablero  # Devuelve el tablero actualizado

