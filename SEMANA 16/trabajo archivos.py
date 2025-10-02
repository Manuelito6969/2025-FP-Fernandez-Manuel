archivo_escritura = open('my_notes.txt', 'w')
archivo_escritura.write("Nota 1: Recordar la evaluacion de mañana.\n")
archivo_escritura.write("Nota 2: Llamar a mi amigo Jonathan por la tarde.\n")
archivo_escritura.write("Nota 3: Terminar el proyecto de Programacion antes del fin de semana.\n")

archivo_escritura.close()

archivo_lectura = open('my_notes.txt', 'r')

print("Contenido del archivo my_notes.txt:")
linea = archivo_lectura.readline()
while linea != "":
    print(linea.strip())
    linea = archivo_lectura.readline()

archivo_lectura.close()
