opciones_validas = {'A', 'B', 'C'}

while True:
    tipo_cliente = input('Ingrese su tipo de cliente (A, B, C): ').strip().upper()

    if tipo_cliente in opciones_validas:
        break

    print('Opción inválida. Ingrese únicamente A, B o C.\n')

print(f'Acceso configurado para: Clase {tipo_cliente}')

while True:
    try:
       monto_total_de_compra = int(input('Ingrese el monto total de la compra: '))
       break
    except ValueError:
        print('Dato erroneo, intente nuevamente.')


if tipo_cliente == 'A':
    if monto_total_de_compra > 1000:
        descuento
    elif monto_total_de_compra 
    