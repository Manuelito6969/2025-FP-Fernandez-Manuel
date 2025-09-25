# Definimos la matriz bidimensional
matriz = [
    [1, 9, 5],
    [7, 3, 2],
    [8, 4, 6]
]


def bubble_sort_fila(matriz, fila_a_ordenar):
    """
    Ordena una fila específica de una matriz usando el algoritmo Bubble Sort.
    """
    # Verificamos si la fila existe en la matriz
    if fila_a_ordenar >= len(matriz):
        print(f"Error: La fila {fila_a_ordenar} no existe.")
        return

    # Obtenemos la fila a ordenar
    fila = matriz[fila_a_ordenar]
    n = len(fila)

    # Bucle principal de Bubble Sort
    for i in range(n - 1):
        # Bucle interno para comparar e intercambiar elementos
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                # Intercambiamos los elementos si están en el orden incorrecto
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


# Fila que queremos ordenar
fila_a_ordenar = 1

# Mostramos la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)

# Llamamos a la función para ordenar la fila
bubble_sort_fila(matriz, fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)