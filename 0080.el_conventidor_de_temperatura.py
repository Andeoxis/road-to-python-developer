def celsius_a_fahrenheit(temperatura):
    return (temperatura * 1.8) + 32

temp = float(input('Ingrese la temperatura en celsius: '))

conversion = celsius_a_fahrenheit(temp)

print('\n---- CONVENTIDOR DE TEMPERATURA ----\n')
print(f'La conversion de celsius a fahrenheit es: {conversion:.1f} fahreheit.')
