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
3: 50,
2: 20,
-2: -20,
-3: -60,
-4: -100

}

# valores =  np.matrix('1 2 3 4 3 2 1; 2 3 4 5 4 3 2; 3 4 5 6 5 4 3; 3 4 5 6 5 4 3; 2 3 4 5 4 3 2; 1 2 3 4 3 2 1')
valores = np.array([
    [1,2,3,4,3,2,1],
    [2,3,4,5,4,3,2],
    [3,4,5,6,5,4,3],
    [3,4,5,6,5,4,3],
    [2,3,4,5,4,3,2],
    [1,2,3,4,3,2,1]
])
#  [1. 2. 3. 4. 3. 2. 1.]
#  [2. 3. 4. 5. 4. 3. 2.]
#  [3. 4. 5. 6. 5. 4. 3.]
#  [3. 4. 5. 6. 5. 4. 3.]
#  [2. 3. 4. 5. 4. 3. 2.]
#  [1. 2. 3. 4. 3. 2. 1.]]
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

def heuristica(puntos_juntos, turno, col, fila):
    if puntos_juntos == 2:
        if turno == 2:
            return 20
        else:
            return -20  
    elif puntos_juntos == 3:
        if turno == 2:
            return 50
        else:
            return -60
    elif puntos_juntos == 4:
        if turno == 2:
            return 100
        else:
            return -100
    elif puntos_juntos == 1:
        return valores[fila][col]
    
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
#  [1. 2. 3. 4. 3. 2. 1.]
#  [2. 3. 4. 5. 4. 3. 2.]
#  [3. 4. 5. 6. 5. 4. 3.]
#  [3. 4. 5. 6. 5. 4. 3.]
#  [2. 3. 4. 5. 4. 3. 2.]
#  [1. 2. 3. 4. 3. 2. 1.]]

def puntos_juntos(tablero, fila, col, turno): #creado por mi
        arrayjuntos = 1
        filauso = fila
        colauso = col
        shift = False
        turnopieza = turno
        diccionario_cantidades = {
            'abajo': 1,
            'diagonal_abajo_izquierda': 1,
            'diagonal_arriba_izquierda': 1,
            'diagonal_abajo_derecha': 1,
            'diagonal_arriba_derecha' : 1,
            'derecha': 1,
            'izquierda': 1
        }
        # if turno == 0:
        #    turnopieza = PIEZA_JUGADOR
        # elif turno == 1:
        #    turnopieza = PIEZA_IA #if tablero[filauso][colauso] == tablero[filauso - 1][colauso] and not 0:
        print('columna elegida ' +str(col))
        # if turno == tablero[filauso + 1][colauso]: #columna abajo 
        if filauso < 5:
          filauso = fila
          colauso = col
          while turnopieza == tablero[filauso + 1][colauso] :
            # arrayjuntos = arrayjuntos + 1
            diccionario_cantidades['abajo'] = diccionario_cantidades['abajo'] + 1
            filauso = filauso + 1
            if filauso == 5:
               break
          # puntos_juntos(tablero, filauso + 1, colauso)
        #   return arrayjuntos
        # elif turnopieza == tablero[filauso][colauso - 1]  : #misma fila columna izquierda
        elif colauso > 0:
            filauso = fila
            colauso = col
            while turnopieza == tablero[filauso][colauso - 1]:#misma fila columna izquierda
            #   arrayjuntos = arrayjuntos + 1
                diccionario_cantidades['izquierda'] = diccionario_cantidades['izquierda'] + 1
                colauso = colauso - 1
                if colauso == 0:
                    break
            filauso = fila #reseet a la posicion original de funcion
            colauso = col
            if colauso < 6:
                while turnopieza == tablero[filauso][colauso + 1]:
                    # arrayjuntos = arrayjuntos + 1
                    diccionario_cantidades['izquierda'] = diccionario_cantidades['izquierda'] + 1
                    colauso = colauso + 1
                    if colauso == 6:
                        break
            #     return arrayjuntos
            # return arrayjuntos
        # elif turnopieza == tablero[filauso][colauso + 1] : #misma fila columna derecha
        
        elif colauso < 6:
            filauso = fila
            colauso = col
            while turnopieza == tablero[filauso][colauso + 1] :#misma fila columna derecha 
            #   arrayjuntos = arrayjuntos + 1
              diccionario_cantidades['derecha'] = diccionario_cantidades['derecha'] + 1
              colauso = colauso + 1
              if colauso == 6:
                  break
            filauso = fila #reseet a la posicion original de funcion
            colauso = col
            if colauso > 0:
                while turnopieza == tablero[filauso][colauso - 1]: 
                    # arrayjuntos = arrayjuntos + 1
                    diccionario_cantidades['derecha'] = diccionario_cantidades['derecha'] + 1
                    colauso = colauso - 1
                    if colauso == 0 :
                        break
            #         return arrayjuntos
            # return arrayjuntos
        # elif turnopieza == tablero[filauso + 1][colauso - 1] :#diagonal izquieda abajo
        elif filauso < 5 or colauso > 0:
            filauso = fila
            colauso = col
            while turnopieza == tablero[filauso + 1][colauso - 1]:#diagonal izquieda abajo
            #    arrayjuntos = arrayjuntos + 1
               diccionario_cantidades['diagonal_abajo_izquierda'] = diccionario_cantidades['derecha'] + 1
               filauso = filauso + 1
               colauso = colauso - 1
               if colauso == 0 or filauso == 5:
                   break
            filauso = fila
            colauso = col
            if filauso > 0 or colauso < 6:
                while turnopieza == tablero[filauso - 1][colauso + 1]: 
                    # arrayjuntos = arrayjuntos + 1
                    diccionario_cantidades['diagonal_abajo_izquierda'] = diccionario_cantidades['diagonal_abajo_izquierda'] + 1
                    filauso = filauso - 1
                    colauso = colauso + 1
                    if colauso == 6 or filauso == 0:
                        break
                #     return arrayjuntos
                # return arrayjuntos
        # elif turnopieza == tablero[filauso - 1][colauso - 1] :#diagonal izquierda arriba
        elif filauso > 0 or colauso > 0:
            filauso = fila
            colauso = col
            while turnopieza == tablero[filauso - 1][colauso - 1]: #diagonal izquierda arriba
            #    arrayjuntos = arrayjuntos + 1
               diccionario_cantidades['diagonal_arriba_izquierda'] = diccionario_cantidades['diagonal_arriba_izquierda'] + 1
               filauso = filauso - 1
               colauso = colauso - 1
               if colauso == 0 or filauso == 0:
                   break
            filauso = fila
            colauso = col
            if filauso < 5 or colauso > 1:
                while turnopieza == tablero[filauso + 1][colauso + 1]: 
                    # arrayjuntos = arrayjuntos + 1
                    diccionario_cantidades['diagonal_arriba_izquierda'] = diccionario_cantidades['diagonal_arriba_izquierda'] + 1
                    filauso = filauso + 1
                    colauso = colauso + 1
                    if colauso == 6 or filauso == 5:
                        break
                #     return arrayjuntos
                # return arrayjuntos
        # elif turnopieza == tablero[filauso - 1][colauso + 1]: #diagonal derecha arriba
        elif filauso > 0 or colauso < 6:
            filauso = fila
            colauso = col
            while turnopieza == tablero[filauso - 1][colauso + 1]: #diagonal derecha arriba
            #    arrayjuntos = arrayjuntos + 1
               diccionario_cantidades['diagonal_arriba_derecha'] = diccionario_cantidades['diagonal_arriba_derecha'] + 1
               filauso = filauso - 1
               colauso = colauso + 1
               if colauso == 6 or filauso == 0:
                   break
            filauso = fila
            colauso = col
            if filauso < 5 or colauso > 0:
                while turnopieza == tablero[filauso + 1][colauso - 1]: 
                    # arrayjuntos = arrayjuntos + 1
                    diccionario_cantidades['diagonal_arriba_derecha'] = diccionario_cantidades['diagonal_arriba_derecha'] + 1
                    filauso = filauso + 1
                    colauso = colauso - 1
                    if colauso == 0 or filauso == 5:
                        break
                # return arrayjuntos
        # elif turnopieza == tablero[filauso + 1][colauso + 1]: #diagonal derecha abajo
        
        elif filauso < 5 or colauso < 6:
            filauso = fila
            colauso = col
            while turnopieza == tablero[filauso + 1][colauso + 1]:
            #    arrayjuntos = arrayjuntos + 1
               diccionario_cantidades['diagonal_abajo_derecha'] = diccionario_cantidades['diagonal_abajo_derecha'] + 1
               filauso = filauso + 1
               colauso = colauso + 1
               if colauso == 6 or filauso == 5:
                   break
            filauso = fila
            colauso = col
            if colauso > 0 or filauso > 0:
                while turnopieza == tablero[filauso - 1][colauso - 1]: 
                    # arrayjuntos = arrayjuntos + 1
                    diccionario_cantidades['diagonal_abajo_derecha'] = diccionario_cantidades['diagonal_abajo_derecha'] + 1
                    filauso = filauso - 1
                    colauso = colauso - 1
                    if colauso == 0 or filauso == 0:
                        break
            # return arrayjuntos
        maximum = max(diccionario_cantidades, key=diccionario_cantidades.get)  # Just use 'min' instead of 'max' for minimum.
        print('mayor cantidad ' +str(diccionario_cantidades[maximum])) 
        return diccionario_cantidades[maximum]
def minimax(tablero, profundidad, alpha, beta, es_maximizando, heuristicareceive=0):
    if profundidad == 0 :
        return heuristicareceive #valor cuando profundidad es 0
    opciones = obtener_columnas_validas(tablero)
    posicionheuristica = {}
    if es_maximizando: 
       turno = PIEZA_IA
    else:
       turno = PIEZA_JUGADOR
    print(opciones)
    for col in opciones: #todas las opciones disponibles del tablero y su heuristica
      opcionfila = obtener_siguiente_fila_libre(tablero, col)
      puntosjuntos = puntos_juntos(tablero, opcionfila, col, turno)#
      print('puntos juntos ' +str(puntosjuntos))
      valor = heuristica(puntosjuntos, turno, col, opcionfila) #heuristica(puntos_juntos, turno, col, fila):
      print('valor heuristico: ' +str(valor))
      posicionheuristica[col] = int(valor)
      print(posicionheuristica) # 0: np.int64(1), 1: np.int64(2), 2: np.int64(3),
      print ('---------------------------------------------------')
      evaluar_ventana 

    if es_maximizando: #nuestra logica :D
        print("Entrar a MAX")
        maxEval = -1000000 #alpha
    #   for col in opciones:
        for colchild, heuristicachild in posicionheuristica.items(): # 0: np.int64(1), 1: np.int64(2), 2: np.int64(3),
            filadisponible = obtener_siguiente_fila_libre(tablero, colchild)
            tablerohijo = tablero
            tablerohijo[filadisponible][colchild] = turno
            print('Evaluar ' +str(colchild))
            eval =  minimax(tablerohijo, profundidad - 1, heuristicachild, beta, False, heuristicachild)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval 
    else:
        minEval = 1000000 #beta
        print("Entrar a MIN")
        for colchild, heuristicachild in posicionheuristica.items():
            filadisponible = obtener_siguiente_fila_libre(tablero, colchild)
            tablerohijo = tablero
            tablerohijo[filadisponible][colchild] = turno
            print('Evaluar ' +str(colchild))
            eval = minimax(tablerohijo, profundidad - 1, alpha, heuristicachild, True,  heuristicachild )
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval
    # RETO: Implementar algoritmo Minimax con Poda Alfa-Beta
    # Debe retornar una tupla (columna, puntuacion)
    pass

# def minmaxPoda(tablero, profundidad, alpha, beta, es_maximizando):
#     opciones = obtener_columnas_validas(tablero)
#     es_terminal = verificar_victoria(tablero, PIEZA_JUGADOR) or verificar_victoria(tablero, PIEZA_IA) or len(opciones) == 0
#     if profundidad == 0 or es_terminal:
#         if es_terminal:
#             if verificar_victoria(tablero, PIEZA_IA):
#                 return (None, 100000000000000)
#             elif verificar_victoria(tablero, PIEZA_JUGADOR):
#                 return (None, -10000000000000)
#             else: # Empate
#                 return (None, 0)
#         else: # Profundidad 0
#             return (None, evaluar_ventana(tablero, PIEZA_IA))
#     if es_maximizando:
#         valor_max = -math.inf
#         columna_elegida = random.choice(opciones)
#         for col in opciones:
#             fila = obtener_siguiente_fila_libre(tablero, col)
#             tablero[fila][col] = PIEZA_IA
#             nueva_puntuacion = minmaxPoda(tablero, profundidad-1, alpha, beta, False)[1]
#             tablero[fila][col] = VACIO
#             if nueva_puntuacion > valor_max:
#                 valor_max = nueva_puntuacion
#                 columna_elegida = col
#             alpha = max(alpha, valor_max)
#             if alpha >= beta:
#                 break
#         return columna_elegida, valor_max
#     else: 
#         valor_min = math.inf
#         columna_elegida = random.choice(opciones)
#         for col in opciones:
#             fila = obtener_siguiente_fila_libre(tablero, col)
#             tablero[fila][col] = PIEZA_JUGADOR
#             nueva_puntuacion = minmaxPoda(tablero, profundidad-1, alpha, beta, True)[1]
#             tablero[fila][col] = VACIO
#             if nueva_puntuacion < valor_min:
#                 valor_min = nueva_puntuacion
#                 columna_elegida = col
#             beta = min(beta, valor_min)
#             if alpha >= beta:
#                 break
#         return columna_elegida, valor_min

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