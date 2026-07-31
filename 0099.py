while True:
    try:
        tipo_de_cliente = input('Ingrese el tipo de cliente que eres ("A"Excelente, "B"Bueno, "C"Regular):\n').lower().strip()
        if tipo_de_cliente not in ['a', 'b', 'c']:
            raise ValueError
        monto_ingresado = int(input('Ingrese el monto en bs: \n'))
        if 0 >= monto_ingresado:
            raise ValueError
        break 
    except ValueError:
        print('ERROR. Intente de nuevo.')
if tipo_de_cliente == 'a':
    if monto_ingresado > 1000:
        descuento = monto_ingresado * 0.20
        total_a_pagar = monto_ingresado - descuento
        print(f'Monto ingresado es de: {monto_ingresado}')
        print(f'Tienes un descuento: {descuento}')
        print(f'Total a pagar es de: {total_a_pagar}')
    elif monto_ingresado <= 1000:
        descuento = monto_ingresado * 0.15
        total_a_pagar = monto_ingresado - descuento
        print(f'Monto ingresado es de: {monto_ingresado}')
        print(f'Tienes un descuento: {descuento}')
        print(f'Total a pagar es de: {total_a_pagar}')
elif tipo_de_cliente == 'b':
    if monto_ingresado > 1000:
        descuento = monto_ingresado * 0.10
        total_a_pagar = monto_ingresado - descuento
        print(f'Monto ingresado es de: {monto_ingresado}')
        print(f'Tienes un descuento: {descuento}')
        print(f'Total a pagar es de: {total_a_pagar}')
    elif monto_ingresado <= 1000:
        descuento = monto_ingresado * 0.05
        total_a_pagar = monto_ingresado - descuento
        print(f'Monto ingresado es de: {monto_ingresado}')
        print(f'Tienes un descuento: {descuento}')
        print(f'Total a pagar es de: {total_a_pagar}')
else:
    print(f'Usted no tiene descuento, usted paga: {monto_ingresado}')