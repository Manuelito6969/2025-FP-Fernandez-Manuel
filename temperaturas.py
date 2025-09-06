# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 40},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 42}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 39},
            {"day": "Miércoles", "temp": 43},
            {"day": "Jueves", "temp": 41},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 37}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 37},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 42},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 41},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 35}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 10},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 10}
        ]
    ]
]

# Lista con los nombres de las ciudades
ciudades = ["Guayaquil", "Quito", "Cuenca"]


# Calcular el promedio de temperaturas para cada ciudad y semana
i=0
for ciudad in temperaturas:
    # Usa el índice 'i' para obtener el nombre de la ciudad
    print(f'\n--- Promedios para {ciudades[i]} ---')
    j=0
    for semana in ciudad:
        j=j+1
        suma = 0
        for dia in semana:
            suma += dia['temp']
        promedio = round(suma / 7, 1)
        print(f'El promedio de la semana No. {j} es: {promedio}°C')
    i=i+1