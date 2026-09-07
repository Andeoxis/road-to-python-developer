def conversor_temperatura(celsius, escala):
    '''Conversor de temperatura'''
    if escala == 'f':
        return (celsius * 9 / 5) + 32
    elif escala == 'k':
        return celsius + 273.15

print(f'\n{conversor_temperatura.__doc__}')

while True:
    try:

        esc = input('Ingrese a que desea convertir f(fahrenheit) o k(kelvin): ').lower().strip()
        if esc not in ('f', 'k'):
            raise ValueError
        
        celsi = float(input('Ingrese la temperatura en C: '))
        if celsi < -273.15:
            raise ValueError
        break

    except ValueError:
        print('\nError. Algo fallo...')
        print('- La escala debe ser únicamente "f" o "k".')
        print('- La temperatura no puede ser menor al cero absoluto (-273.15 °C).\n')

resultado = conversor_temperatura(celsi, esc)
if esc == 'f':
    unidad = 'f'
else:
    unidad = 'k'
print(f'Resultado: {resultado:.2f} {unidad}')