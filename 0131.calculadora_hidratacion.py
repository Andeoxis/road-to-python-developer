def calculadora_de_hidratacion(peso, minutos_ejercicio):
    '''Calculadora de hidratacion'''
    return ((peso * 35) + ((minutos_ejercicio / 30) * 500)) / 1000
print(f'\n{calculadora_de_hidratacion.__doc__}')

while True:
    try:

        pes = float(input('Ingrese el peso en kg: '))
        if pes <= 0 or pes > 300:
            raise ValueError
        min_eje = float(input('Ingrese los minutos de ejercicio que hace: '))
        if min_eje < 0 or min_eje > 360:
            raise ValueError
        break

    except ValueError:
        print('ERROR.')

resultado = calculadora_de_hidratacion(pes, min_eje)
print(f'Resultado: Consumir {resultado:.2f} litros de agua al dia')