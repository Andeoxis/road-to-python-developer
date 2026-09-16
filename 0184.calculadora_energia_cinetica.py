def calcular_energia_cinetica(masa, velocidad):
    '''Calculadora de energia cinetica'''
    return 1/2 * masa * velocidad ** 2

print(f'\n{calcular_energia_cinetica.__doc__}')

while True:
    try:
        mas = float(input('Ingrese la masa en kg: '))
        if mas <= 0 or mas > 50000:
            raise ValueError
        velo = float(input('Ingrese la velocidad en metros por segundo: '))
        if velo < 0 or velo > 1000:            
            raise ValueError
        break

    except ValueError:
        print('Error: Algo fallo.')
        print('Intente nuevamente.')

resultado = calcular_energia_cinetica(mas, velo)
print(f'Resultado: {resultado:.2f} joules')