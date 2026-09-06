def calculadora_descuento(precio, descuento):
    '''Calculadora de descuento'''
    monto_descuento = precio * (descuento / 100)
    precio_final = precio - monto_descuento
    return monto_descuento, precio_final

print(f'\n{calculadora_descuento.__doc__}')

while True:
    try:
        prec = float(input('Ingrese el precio del producto: '))
        descu = float(input('Ingrese el descuento del 0 al 100: '))
        if prec <= 0 or descu < 0 or descu > 100:
            raise ValueError
        break
    except ValueError:
        print('ERROR. Solo puedes colocar numeros')
        print('No puedes colocar precios negativos')
        print('No puedes colocar un descuento fuera del rango')
        print('Intente nuevamente.')

ahorro, total = calculadora_descuento(prec, descu)
print(f'Resultado: Tu descuento es: {ahorro:.2f} y debes pagar un total de: {total:.2f}')