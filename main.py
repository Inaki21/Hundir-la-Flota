import utils
import random
import numpy as np
import time
from variables import simbolo_agua , simbolo_barco, simbolo_fallo, simbolo_impacto

def turno_jugador(tablero): # Define una función llamada turno_jugador que toma un tablero como argumento
    tablero = utils.disparo(tablero) # Llama a la función disparo del módulo utils, que permite al jugador disparar y actualiza el tablero
    time.sleep(1) # Pausa la ejecución por 1 segundos para que el juego no vaya demasiado rápido en la consola
    return tablero  # Devuelve el tablero actualizado

def turno_maquina(tablero):  # Define una función llamada turno_maquina que toma un tablero como argumento
    while True: # Inicia un bucle infinito que se ejecutará hasta que se rompa con un "break"        
        x = random.randint(0, 9)  # Genera un número aleatorio entre 0 y 9 para la fila   
        y = random.randint(0, 9)  # para la columna    
        if tablero[x, y] in [simbolo_agua, simbolo_barco]:  # Verifica si la posición en el tablero está vacía ('_') o tiene un barco ('O')    
            if tablero[x, y] == simbolo_barco: # Si la posición tiene un barco ('O')  
                tablero[x, y] = simbolo_impacto  # Marca la posición como impactada ('X')    
                print("_"*70)
                print()
                print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
                print(f"La máquina ha disparado en ({x}, {y}) y ha dado en el blanco.")
                print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
                print("_"*70) 
            
                vuelve_a_disparar = True # Se declara la varriable vuelve_a_disparar a True            
            else: # si no
                tablero[x, y] = simbolo_fallo # Marca la posición como fallo ('#')
                print("_"*70)
                print()
                print("🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊")
                print(f"La máquina ha disparado en ({x}, {y}) y ha fallado.")
                print("🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊")
                print("_"*70)
                vuelve_a_disparar = False # la variable a False
            break  # Rompe el bucle infinito después de que la máquina haya disparado
    
    if vuelve_a_disparar:
        time.sleep(1)
        return turno_maquina(tablero)
        
    else:
        time.sleep(1)
        return tablero # Devuelve el tablero actualizado 

def juego_completo(): # Define una función llamada juego_completo

    tablero_jugador_barcos = utils.crear_tablero() # Crea un tablero para los barcos del jugador
    tablero_rival_barcos = utils.crear_tablero() # Crea un tablero para los barcos del rival
    
    '''tablero_rival_disparos = utils.crear_tablero()  # Crea un tablero para los disparos del rival
    tablero_jugador_disparos = utils.crear_tablero() # Crea un tablero para los disparos del jugador'''

    utils.colocar_barcos(tablero_jugador_barcos) # Coloca los barcos del jugador de manera aleatoria
    utils.colocar_barcos(tablero_rival_barcos) # Coloca los barcos del rival de manera aleatoria
 
    while True:  # Inicia un bucle infinito hasta el "break"
        print("Tablero del jugador (Barcos del jugador y disparos del rival):")  # Imprime un mensaje indicando el tablero del jugador
        print(tablero_jugador_barcos)  # Imprime el tablero de los barcos del jugador
        time.sleep(1) # Pausa la ejecución por 1 segundos
        print("Tablero de disparos del jugador:") # Imprime un mensaje indicando el tablero de disparos del jugador
        print(tablero_rival_barcos) # Imprime el tablero de los barcos del rival
        tablero_rival_barcos = turno_jugador(tablero_rival_barcos) # Llama a la función turno_jugador para que el jugador dispare
        if np.all(tablero_rival_barcos == simbolo_impacto):  # Verifica si todos los barcos del rival han sido impactados
            print(" Goazen Glorioso! Hay demasiados barcos para llegar a hundirlos todos") # Informa al jugador que ha ganado
            break  # Rompe el bucle infinito si el jugador ha ganado

        tablero_jugador_barcos = turno_maquina(tablero_jugador_barcos) # Llama a la función turno_maquina para que la máquina dispare
        if np.all(tablero_jugador_barcos == simbolo_impacto): # Verifica si todos los barcos del jugador han sido impactados
            print(" you loose vs machine ")  # Informa al jugador que la máquina ha ganado
            break  # Rompe el bucle infinito si la máquina ha ganado

if __name__ == "__main__":   # Verifica si el script se está ejecutando como programa principal
    juego_completo()  # Llama a la función juego_completo para iniciar el juego