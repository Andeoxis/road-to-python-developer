temperaturas = []

for i in range(1,6):
    while True:
        try:
            temp = int(input(f'Dame la temperatura del servidor N{i}:\n'))
            temperaturas.append(temp)
            break
        except ValueError:
            print('ERROR: Solo puedes colocar numeros, intenta de nuevo.')

promedio = sum(temperaturas) / 5

temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)

print('\n---- REPORTE DEL SISTEMA ----')
print(f'Promedio de temperatura: {promedio}C')
print(f'Temperatura mas alta: {temperatura_maxima}C')
print(f'Temperatura mas baja: {temperatura_minima}C')
print('--------------------')