# DEFINIR FUNCIONES

def calcular_iva(subtotal, porcentaje_iva):
    valor_iva = subtotal * (porcentaje_iva/100)
    return valor_iva


subtotal = float(input("Ingrese el valor del subtotal: "))
porcentaje_iva = float(input("Ingrese el porcentaje del iva: "))

# LLAMADA A LA FUNCION
valor_iva = calcular_iva(subtotal, porcentaje_iva)
valor_total = subtotal + valor_iva

print(f'El valor subtotal es: {subtotal}')
print(f'El porcentaje de iva es: {porcentaje_iva}')
print(f'El valor de iva es: {valor_iva}')
print(f'El valor total es: {valor_total}')