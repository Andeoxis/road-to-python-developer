def calcular_fuerza_centripeta(masa, velocidad, radio):
    '''Calculadora de fuerza centripeta'''
    return (masa * velocidad ** 2) / radio

print(f'\n{calcular_fuerza_centripeta.__doc__}')

while True:
    try:
        masa_ = float(input('Ingrese la masa en kg: '))
        if masa_ < 0 and masa_ >= 10000:
            raise ValueError

        velocidad_ = float(input('Ingrese en metros por segundo: '))
        radio_ = float(input('Ingrese la curva o trayectoria en metros: '))
        break
    except ValueError:
        print('Error: Algo fallo...')
        print('Intenta nuevamente.')


