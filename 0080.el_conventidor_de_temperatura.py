def celsius_a_fahrenheit(temperatura):
    return (temperatura * 1.8) + 32
while True:
    try:
        temp = float(input('Ingrese la temperatura en celsius: '))
        break
    except ValueError:
        print('ERROR: Dato incorrecto.')
        print('Intente nuevamente.')

conversion = celsius_a_fahrenheit(temp)

print('\n---- CONVENTIDOR DE TEMPERATURA ----\n')
print(f'La conversion de celsius a fahrenheit es: {conversion:.1f} fahreheit.')
