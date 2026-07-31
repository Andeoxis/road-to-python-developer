while True:
    try:
        monto_de_compra = float(input('Ingrese su monto de compra:\n'))
        break
    except ValueError:
        print('Error. Intenta nuevamente.')

if monto_de_compra > 500:
    descuento = monto_de_compra * 0.10
    total_a_pagar = monto_de_compra - descuento
    print(f'Monto ingresado es de: {monto_de_compra}')
    print(f'Tienes un descuento de: {descuento}')
    print(f'Total a pagar es de: {total_a_pagar}')
else:
    print(f'Monto ingresado es de: {monto_de_compra}')
    print(f'No tienes descuento.')

