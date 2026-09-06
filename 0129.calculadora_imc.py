def calculadora_imc (peso, altura):
    '''Calculadora de imc'''
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return imc, 'Bajo peso'
    elif 18.5 <= imc < 25.0:
        return imc, 'Peso normal'
    elif 25.0 <= imc < 30.0:
        return imc, 'Sobrepeso'
    elif imc >= 30.0:
        return imc, 'Obesidad'

print(f'\n{calculadora_imc.__doc__}')

while True:
    try:
        pes = float(input('Ingrese su peso en kg: '))
        altu = float(input('Ingrese su altura en metros: '))
        if pes <= 0 or pes > 400 or altu < 0.5 or altu > 2.5:
            raise ValueError
        break

    except ValueError:
        print('ERROR. Algo fallo')
        print('El peso debe estar en el rango de 0 a 400 kg')
        print('La altura debe estar en el rango de 0.5 a 2.5 metros')

imc, clasificacion = calculadora_imc(pes, altu)
print('Resultado:')
print(f'Tu imc es: {imc:.1f} y tu categoria asignada es: {clasificacion}')