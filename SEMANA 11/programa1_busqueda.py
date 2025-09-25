    # Definimos la matriz bidimensional
matriz = [
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11]
]
# Definimos el valor que queremos buscar
valor_a_buscar = 6


def buscar_en_matriz(matriz, valor):
    """
    Busca un valor en una matriz bidimensional y devuelve su posición.
    """
    # Recorremos la matriz fila por fila y columna por columna
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            # Si el valor de la celda es igual al valor que buscamos
            if matriz[fila][columna] == valor:
                # Retornamos las coordenadas de la fila y la columna
                return (fila, columna)

    # Si el bucle termina y no se encontró el valor, retornamos None
    return None


# Llamamos a la función para buscar el valor
posicion = buscar_en_matriz(matriz, valor_a_buscar)

# Verificamos si se encontró el valor y mostramos el resultado
if posicion:
    # Si se encontró, 'posicion' contendrá las coordenadas
    fila_encontrada, columna_encontrada = posicion
    print(f"El valor {valor_a_buscar} se encontró en la posición ({fila_encontrada}, {columna_encontrada}).")
else:
    # Si no se encontró, 'posicion' será None
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
