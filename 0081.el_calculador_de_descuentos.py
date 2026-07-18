def obtener_descuento(monto):
    return 0.15 if monto > 200 else 0.0

try:
    precio_de_compra = float(input('Ingrese el costo total de la compra (Bs): '))
    if precio_de_compra < 0:
        raise ValueError
    
    porcentaje = obtener_descuento(precio_de_compra)

    tiene_descuento = porcentaje > 0
    estado = 'Tienes descuento (15%)' if tiene_descuento else 'No tienes descuento'

    monto_final = precio_de_compra * (1 - porcentaje)

    print('\n---- CALCULADOR DE DESCUENTO ----')
    print(f'Tu estado final es: {estado}')
    print(f'El monto final a pagar es de: {monto_final:.2f}')

except ValueError:
    print('ERROR: Ingrese un monto numerico valido y mayor a cero.')