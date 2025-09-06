# Definir nombres de ciudades y semanas para que el resultado sea más claro
ciudades = ["Quito", "Guayaquil"]
semanas = ["Semana 1", "Semana 2"]

# Matriz 3D: [Ciudades] -> [Semanas] -> [Temperaturas_por_dia]
temperaturas_ciudades = [
    # Datos para Quito
    [
        [15, 16, 17, 18, 17, 16, 15],  # Semana 1 de Quito
        [14, 15, 15, 16, 17, 16, 15]  # Semana 2 de Quito
    ],
    # Datos para Guayaquil
    [
        [28, 29, 30, 29, 28, 27, 28],  # Semana 1 de Guayaquil
        [29, 30, 31, 30, 29, 28, 29]  # Semana 2 de Guayaquil
    ]
]

# Bucle para recorrer las ciudades
for i in range(len(temperaturas_ciudades)):
    # Bucle anidado para recorrer las semanas de cada ciudad
    for j in range(len(temperaturas_ciudades[i])):
        # Inicializar la suma de temperaturas para esta semana
        suma_temperaturas = 0
        # Bucle anidado para sumar las temperaturas de cada día de la semana
        for k in range(len(temperaturas_ciudades[i][j])):
            # Sumar la temperatura del día actual
            suma_temperaturas += temperaturas_ciudades[i][j][k]

        # Calcular el promedio de temperaturas para la semana
        promedio_semanal = suma_temperaturas / len(temperaturas_ciudades[i][j])

        # Mostrar el resultado de forma clara
        print(f"El promedio de la {semanas[j]} en {ciudades[i]} fue: {promedio_semanal:.2f}°C")