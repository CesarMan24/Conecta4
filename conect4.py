#hola desde vs 
import numpy as np
import random
import math
import heapq
# Constantes del Juego
FILAS = 6
COLUMNAS = 7
VACIO = 0
PIEZA_JUGADOR = 1
PIEZA_IA = 2

puntaje = {
4: 100,
3: 75,
2: 50,
}
#4 EN LINEA = 100
#3 EN LIENA = 75
#2 EN LINEA = 50
#2 EN CONTRA = -50
#3 EN CONTRA = -75
#4 EN CONTRA = -100
def crear_tablero():
    return np.zeros((FILAS, COLUMNAS))

def obtener_siguiente_fila_libre(tablero, col):
    for f in range(FILAS):
        if tablero[f][col] == 0:
            return f

def verificar_victoria(tablero, pieza):
    imprimir_tablero(tablero)
    #Hotizontal
    for c in range(COLUMNAS - 3):
        for f in range(FILAS):
            if tablero[f][c] == pieza and tablero[f][c+1] == pieza and tablero[f][c+2] == pieza and tablero[f][c+3] == pieza:
                return True
    #Vertical
    for c in range(COLUMNAS):
       for f in range(FILAS - 3):
            if tablero[f][c] == pieza and tablero[f+1][c] == pieza and tablero[f+2][c] == pieza and tablero[f+3][c] == pieza:
                return True
    #Diagonal 1
    for c in range(COLUMNAS - 3):
        for f in range(FILAS - 3):
              if tablero[f][c] == pieza and tablero[f+1][c+1] == pieza and tablero[f+2][c+2] == pieza and tablero[f+3][c+3] == pieza:
                  return True

    #Diagonal 2
    for c in range(COLUMNAS - 3):
        for f in range(3, FILAS):
              if tablero[f][c] == pieza and tablero[f-1][c+1] == pieza and tablero[f-2][c+2] == pieza and tablero[f-3][c+3] == pieza:
                  return True

  

def evaluar_ventana(ventana, pieza):
   
    
    puntuacion = 0
    piezaActual = PIEZA_IA
    if pieza == PIEZA_JUGADOR:
      piezaActual = PIEZA_JUGADOR
      if ventana.count(piezaActual) == 4:
        puntuacion = puntuacion + puntaje[4]
      elif ventana.count(piezaActual) == 3 and ventana.count(VACIO) == 1:
        puntuacion = puntuacion + puntaje[3]
      elif ventana.count(piezaActual) == 2 and ventana.count(VACIO) == 2:
        puntuacion = puntuacion + puntaje[2]

    if ventana.count(piezaActual) == 4 and ventana.count(VACIO)==1:
        puntuacion = puntuacion - puntaje[4]  
    
    return puntuacion

def heuristica(puntos_juntos, turno):
    if puntos_juntos == 2:
        return 20
    if puntos_juntos == 3:
       return 50
    if puntos_juntos == 4:
       return 100
    
# IA ingresa una ficha sin secuencia
# Valor de la celda asignada puntos
# IA va a llegar a  dos fichas juntas
# 20 puntos
# IA va a llegar a  tres fichas juntas
# 50 puntos
# IA tiene cuatro fichas juntas
# 100 puntos
# Oponente va a llegar a dos fichas juntas 
# -20 puntos
# Oponente va a llegar a tres fichas juntas
# -60 puntos
# Oponente va a llegar a cuatro fichas juntas
# -100 puntos


def puntos_juntos(tablero, fila, col, turno): #creado por mi
        arrayjuntos = 1
        filauso = fila
        colauso = col
        shift = False
        turnopieza = 0
        # if turno == 0:
        #    turnopieza = PIEZA_JUGADOR
        # elif turno == 1:
        #    turnopieza = PIEZA_IA #if tablero[filauso][colauso] == tablero[filauso - 1][colauso] and not 0:

        if turno == tablero[filauso - 1][colauso]: #columna abajo 
          # filauso = fila + 1
          # arrayjuntos = arrayjuntos + 1
          while turnopieza == tablero[filauso - 1][colauso] :
            arrayjuntos = arrayjuntos + 1
            filauso = filauso - 1
            if filauso == 5:
               break
          # puntos_juntos(tablero, filauso + 1, colauso)
          return arrayjuntos
        elif turnopieza == tablero[filauso][colauso - 1]  : #misma fila columna izquierda
            while turnopieza == tablero[filauso][colauso -1]:
              arrayjuntos = arrayjuntos + 1
              colauso = colauso - 1
            filauso = fila #reseet a la posicion original de funcion
            colauso = col
            while turnopieza == tablero[filauso][colauso + 1]:
              arrayjuntos = arrayjuntos + 1
              colauso = colauso + 1
              if colauso == 6:
               break
            return arrayjuntos
        elif turnopieza == tablero[filauso][colauso + 1] : #misma fila columna derecha
            while turnopieza == tablero[filauso][colauso + 1] :
              arrayjuntos = arrayjuntos + 1
              colauso = colauso + 1
            filauso = fila #reseet a la posicion original de funcion
            colauso = col
            while turnopieza == tablero[filauso][colauso - 1] and (colauso - 1) <= 6: 
              arrayjuntos = arrayjuntos + 1
              colauso = colauso - 1
              if colauso == 6 or filauso == 5:
               break
            return arrayjuntos
        elif turnopieza == tablero[filauso - 1][colauso - 1] :#diagonal izquieda abajo
            while turnopieza == tablero[filauso - 1][colauso - 1]:
               arrayjuntos = arrayjuntos + 1
               filauso = filauso - 1
               colauso = colauso - 1
            filauso = fila
            colauso = col
            while turnopieza == tablero[filauso + 1][colauso + 1]: 
               arrayjuntos = arrayjuntos + 1
               filauso = filauso - 1
               colauso = colauso - 1
            return arrayjuntos
        elif turnopieza == tablero[filauso + 1][colauso + 1] :#diagonal izquierda arriba
            while turnopieza == tablero[filauso - 1][colauso - 1]:
               arrayjuntos = arrayjuntos + 1
               filauso = filauso + 1
               colauso = colauso + 1
            filauso = fila
            colauso = col
            while turnopieza == tablero[filauso + 1][colauso + 1]: 
               arrayjuntos = arrayjuntos + 1
               filauso = filauso - 1
               colauso = colauso - 1
            return arrayjuntos
def minimax(tablero, profundidad, alpha, beta, es_maximizando):
    opciones = obtener_columnas_validas(tablero)
    posicionheuristica = {}
    
    if es_maximizando: 
       turno = PIEZA_IA
    else:
       turno = PIEZA_JUGADOR
    for col in opciones: #for opcione in opciones:
      opcionfila = obtener_siguiente_fila_libre(tablero, col)
      puntosjuntos = puntos_juntos(tablero, opcionfila, col, turno)#
      valor = heuristica(puntosjuntos, turno )
      posicionheuristica[col] = valor
      evaluar_ventana
    
    if es_maximizando: #nuestra logica :D
      maxEval = alpha
      for opcione in opciones:
        eval =  minimax(tablero, profundidad - 1, alpha, beta, False)
        maxEval = max(maxEval, eval)
        alpha = max(alpha, eval)
        if beta <= alpha:
          break
      return maxEval
    else:
      minEval = beta

    # RETO: Implementar algoritmo Minimax con Poda Alfa-Beta
    # Debe retornar una tupla (columna, puntuacion)
    pass

def obtener_columnas_validas(tablero):
    return [c for c in range(COLUMNAS) if tablero[FILAS-1][c] == 0]

def imprimir_tablero(tablero):
    # Volteamos el tablero para que la fila 0 sea la de abajo
    print(np.flip(tablero, 0))

def jugar():
    tablero = crear_tablero()
    game_over = False
    turno = random.randint(0, 1) # 0 para Humano, 1 para IA
    arbol_por_niveles = {}
    minmax = True
    while not game_over:
        if turno == 0: # Turno Humano / Oponente Manual
            col = int(input("Jugada del Oponente (0-6): "))
            if tablero[FILAS-1][col] == 0:
                fila = obtener_siguiente_fila_libre(tablero, col)
                tablero[fila][col] = PIEZA_JUGADOR
                turno = 1
        else: # Turno de tu IA
            print("IA pensando...")
            col, score = minimax(tablero, 4, -math.inf, math.inf, minmax) #turno
            # col = random.choice(obtener_columnas_validas(tablero))
            fila = obtener_siguiente_fila_libre(tablero, col)
            tablero[fila][col] = PIEZA_IA
            print(f"La IA eligió la columna: {col}")
            turno = 0
            # if minmax: #evaluar uno en maximo-minimo-maximo
            #   minmax = False
            # else:
            #   minmax = True

        imprimir_tablero(tablero)
        # RETO: Añadir condición de salida si alguien gana o se llena el tablero
        

if __name__ == "__main__":
    jugar()