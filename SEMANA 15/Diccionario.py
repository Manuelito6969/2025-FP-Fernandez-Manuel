# Información personal

informacion_personal = {
    "nombre": "Manuel Fernandez",
    "edad": 25,
    "ciudad": "Zamora",
    "profesion": "Estudiante"
}

informacion_personal["ciudad"] = "Cuenca"  # Cambio la ciudad a Cuenca



informacion_personal["profesion"] = "Analista de Sistemas"

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0990353109"

del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)

