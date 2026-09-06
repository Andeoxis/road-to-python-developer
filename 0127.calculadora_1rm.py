def calculadora_1rm (peso, repeticiones):
    '''Calculadora de 1rm'''
    if repeticiones == 1:
        return peso
    return peso * (1 + repeticiones / 30)

print(f'\n{calculadora_1rm.__doc__}')

while True:
    try:
        pes = float(input('Ingrese el peso en kg: '))
        rep = int(input('Ingrese las repeticiones: '))
        if pes <= 0 or rep < 1 or rep > 12:
            raise ValueError
        break

    except ValueError:
        print('ERROR. Algo fallo intenta nuevamente...')
        print('No puedes ingresear mas de 12 repeteciones...')
        print('Porque la formula deja de ser muy precisa apartir de las 12 reps')

resultado = calculadora_1rm(pes, rep)
print(f'Resultado: {resultado:.1f}')